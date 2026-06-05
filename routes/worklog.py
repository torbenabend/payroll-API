from fastapi import APIRouter, Depends, HTTPException

from models import WorkLog
from dependencies.services import get_worklog_service

router = APIRouter(prefix="/worklogs", tags=["WorkLogs"])


@router.get("")
def list_worklogs(service = Depends(get_worklog_service)):
    return service.list_worklogs()


@router.post("")
def create_worklog(
        new_worklog: WorkLog,
        service = Depends(get_worklog_service)
):
    return service.create_worklog(new_worklog)


@router.get("/{worklog_id}")
def get_worklog(
        worklog_id: int,
        service = Depends(get_worklog_service)
):
    worklog = service.get_worklog(worklog_id)
    if worklog is None:
        raise HTTPException(
            status_code=404,
            detail=f"WorkLog with ID {worklog_id} not found"
        )
    return worklog


@router.delete("/{worklog_id}")
def delete_worklog(
        worklog_id: int,
        service = Depends(get_worklog_service)
):
    deleted_worklog = service.delete_worklog(worklog_id)
    if deleted_worklog is None:
        raise HTTPException(
            status_code=404,
            detail=f"WorkLog with ID {worklog_id} not found"
        )
    return deleted_worklog


@router.put("/{worklog_id}")
def update_worklog(
        worklog: WorkLog,
        service = Depends(get_worklog_service)
):
    updated_worklog = service.update_worklog(worklog)
    if updated_worklog is None:
        raise HTTPException(
            status_code=404,
            detail=f"WorkLog with ID {worklog.id} not found"
        )
    return updated_worklog
