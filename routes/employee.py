from datetime import date
from fastapi import APIRouter, Depends, HTTPException

from models import Employee
from dependencies.services import get_employee_service, get_contract_service, get_worklog_service


router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/active_employees")
def list_active_employees(
        expiry_date: date,
        service = Depends(get_employee_service)
):
    return service.list_active_employees(expiry_date)


@router.get("")
def list_employees(service = Depends(get_employee_service)):
    return service.list_employees()


@router.post("")
def create_employee(
        new_employee: Employee,
        service = Depends(get_employee_service)
):
    return service.create_employee(new_employee)


@router.get("/{employee_id}")
def get_employee(
        employee_id: int,
        service = Depends(get_employee_service)
):
    employee = service.get_employee(employee_id)
    if employee is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with ID {employee_id} not found"
        )
    return employee


@router.delete("/{employee_id}")
def delete_employee(
        employee_id: int,
        service = Depends(get_employee_service)
):
    deleted_employee = service.delete_employee(employee_id)
    if deleted_employee is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with ID {employee_id} not found"
        )
    return deleted_employee


@router.put("/{employee_id}")
def update_employee(
        employee: Employee,
        service = Depends(get_employee_service)
):
    updated_employee = service.update_employee(employee)
    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with ID {employee.id} not found"
        )
    return updated_employee


@router.get("/{employee_id}/contracts")
def get_employee_contracts(
        employee_id: int,
        service = Depends(get_contract_service)
):
    return service.get_employee_contracts(employee_id)


@router.get("/{employee_id}/worklogs/{year}/{month}")
def get_employee_worklogs(
        employee_id: int,
        year: int,
        month: int,
        service = Depends(get_worklog_service)
):
    return service.get_employee_worklogs_by_month(employee_id, month, year)
