"""
Functions for interacting with task run ORM objects.
Intended for internal use by the Orion API.
"""

import contextlib
from typing import List
from uuid import UUID

import pendulum
import sqlalchemy as sa
from sqlalchemy import delete, select

from prefect.orion import models, schemas
from prefect.orion.models import orm
from prefect.orion.orchestration.core_policy import CoreTaskPolicy
from prefect.orion.orchestration.global_policy import GlobalTaskPolicy
from prefect.orion.orchestration.rules import (
    OrchestrationResult,
    TaskOrchestrationContext,
)
from prefect.orion.utilities.database import dialect_specific_insert


async def create_task_run(
    session: sa.orm.Session, task_run: schemas.core.TaskRun
) -> orm.TaskRun:
    """
    Creates a new task run.

    If a task run with the same flow_run_id, task_key, and dynamic_key already exists,
    the existing task run will be returned. If the provided task run has a state
    attached, it will also be created.

    Args:
        session: a database session
        task_run: a task run model

    Returns:
        orm.TaskRun: the newly-created or existing task run
    """

    now = pendulum.now("UTC")

    # if a dynamic key exists, we need to guard against conflicts
    insert_stmt = (
        dialect_specific_insert(orm.TaskRun)
        .values(**task_run.dict(shallow=True, exclude={"state"}, exclude_unset=True))
        .on_conflict_do_nothing(
            index_elements=["flow_run_id", "task_key", "dynamic_key"],
        )
    )
    await session.execute(insert_stmt)

    query = (
        sa.select(orm.TaskRun)
        .where(
            sa.and_(
                orm.TaskRun.flow_run_id == task_run.flow_run_id,
                orm.TaskRun.task_key == task_run.task_key,
                orm.TaskRun.dynamic_key == task_run.dynamic_key,
            )
        )
        .limit(1)
        .execution_options(populate_existing=True)
    )
    result = await session.execute(query)
    model = result.scalar()

    if model.created >= now and task_run.state:
        await models.task_runs.set_task_run_state(
            session=session,
            task_run_id=model.id,
            state=task_run.state,
            force=True,
        )
    return model


async def read_task_run(session: sa.orm.Session, task_run_id: UUID) -> orm.TaskRun:
    """
    Read a task run by id.

    Args:
        session: a database session
        task_run_id: the task run id

    Returns:
        orm.TaskRun: the task run
    """

    model = await session.get(orm.TaskRun, task_run_id)
    return model


def _apply_task_run_filters(
    query,
    flow_filter: schemas.filters.FlowFilter = None,
    flow_run_filter: schemas.filters.FlowRunFilter = None,
    task_run_filter: schemas.filters.TaskRunFilter = None,
    deployment_filter: schemas.filters.DeploymentFilter = None,
):
    """
    Applies filters to a task run query as a combination of EXISTS subqueries.
    """

    if task_run_filter:
        query = query.where(task_run_filter.as_sql_filter())

    if flow_filter or flow_run_filter or deployment_filter:
        exists_clause = select(orm.FlowRun).where(
            orm.FlowRun.id == orm.TaskRun.flow_run_id
        )

        if flow_run_filter:
            exists_clause = exists_clause.where(flow_run_filter.as_sql_filter())

        if flow_filter:
            exists_clause = exists_clause.join(
                orm.Flow,
                orm.Flow.id == orm.FlowRun.flow_id,
            ).where(flow_filter.as_sql_filter())

        if deployment_filter:
            exists_clause = exists_clause.join(
                orm.Deployment, orm.Deployment.id == orm.FlowRun.deployment_id
            ).where(deployment_filter.as_sql_filter())

        query = query.where(exists_clause.exists())

    return query


async def read_task_runs(
    session: sa.orm.Session,
    flow_filter: schemas.filters.FlowFilter = None,
    flow_run_filter: schemas.filters.FlowRunFilter = None,
    task_run_filter: schemas.filters.TaskRunFilter = None,
    deployment_filter: schemas.filters.DeploymentFilter = None,
    offset: int = None,
    limit: int = None,
    sort: schemas.sorting.TaskRunSort = schemas.sorting.TaskRunSort.ID_DESC,
) -> List[orm.TaskRun]:
    """
    Read task runs.

    Args:
        session: a database session
        flow_filter: only select task runs whose flows match these filters
        flow_run_filter: only select task runs whose flow runs match these filters
        task_run_filter: only select task runs that match these filters
        deployment_filter: only select task runs whose deployments match these filters
        offset: Query offset
        limit: Query limit
        sort: Query sort

    Returns:
        List[orm.TaskRun]: the task runs
    """

    query = select(orm.TaskRun).order_by(sort.as_sql_sort())

    query = _apply_task_run_filters(
        query,
        flow_filter=flow_filter,
        flow_run_filter=flow_run_filter,
        task_run_filter=task_run_filter,
        deployment_filter=deployment_filter,
    )

    if offset is not None:
        query = query.offset(offset)

    if limit is not None:
        query = query.limit(limit)

    result = await session.execute(query)
    return result.scalars().unique().all()


async def count_task_runs(
    session: sa.orm.Session,
    flow_filter: schemas.filters.FlowFilter = None,
    flow_run_filter: schemas.filters.FlowRunFilter = None,
    task_run_filter: schemas.filters.TaskRunFilter = None,
    deployment_filter: schemas.filters.DeploymentFilter = None,
) -> int:
    """
    Count task runs.

    Args:
        session: a database session
        flow_filter: only count task runs whose flows match these filters
        flow_run_filter: only count task runs whose flow runs match these filters
        task_run_filter: only count task runs that match these filters
        deployment_filter: only count task runs whose deployments match these filters
    Returns:
        int: count of task runs
    """

    query = select(sa.func.count(sa.text("*"))).select_from(orm.TaskRun)

    query = _apply_task_run_filters(
        query,
        flow_filter=flow_filter,
        flow_run_filter=flow_run_filter,
        task_run_filter=task_run_filter,
        deployment_filter=deployment_filter,
    )

    result = await session.execute(query)
    return result.scalar()


async def delete_task_run(session: sa.orm.Session, task_run_id: UUID) -> bool:
    """
    Delete a task run by id.

    Args:
        session: a database session
        task_run_id: the task run id to delete

    Returns:
        bool: whether or not the task run was deleted
    """

    result = await session.execute(
        delete(orm.TaskRun).where(orm.TaskRun.id == task_run_id)
    )
    return result.rowcount > 0


async def set_task_run_state(
    session: sa.orm.Session,
    task_run_id: UUID,
    state: schemas.states.State,
    force: bool = False,
) -> orm.TaskRunState:
    """
    Creates a new orchestrated task run state.

    Setting a new state on a run is the one of the principal actions that is governed by
    Orion's orchestration logic. Setting a new run state will not guarantee creation,
    but instead trigger orchestration rules to govern the proposed `state` input. If
    the state is considered valid, it will be written to the database. Otherwise, a
    it's possible a different state, or no state, will be created. A `force` flag is
    supplied to bypass a subset of orchestration logic.

    Args:
        session: a database session
        task_run_id: the task run id
        state: a task run state model
        force: if False, orchestration rules will be applied that may alter or prevent
            the state transition. If True, orchestration rules are not applied.

    Returns:
        OrchestrationResult object
    """

    # load the task run
    run = await models.task_runs.read_task_run(session=session, task_run_id=task_run_id)

    if not run:
        raise ValueError(f"Invalid task run: {task_run_id}")

    initial_state = run.state.as_state() if run.state else None
    initial_state_type = initial_state.type if initial_state else None
    proposed_state_type = state.type if state else None
    intended_transition = (initial_state_type, proposed_state_type)

    if force:
        orchestration_rules = []
    else:
        orchestration_rules = CoreTaskPolicy.compile_transition_rules(
            *intended_transition
        )

    global_rules = GlobalTaskPolicy.compile_transition_rules(*intended_transition)

    context = TaskOrchestrationContext(
        session=session,
        run=run,
        initial_state=initial_state,
        proposed_state=state,
    )

    # apply orchestration rules and create the new task run state
    async with contextlib.AsyncExitStack() as stack:
        for rule in orchestration_rules:
            context = await stack.enter_async_context(
                rule(context, *intended_transition)
            )

        for rule in global_rules:
            context = await stack.enter_async_context(rule(context))

        await context.validate_proposed_state()

    await session.flush()

    result = OrchestrationResult(
        state=context.validated_state,
        status=context.response_status,
        details=context.response_details,
    )

    return result
