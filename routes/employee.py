from datetime import date
from fastapi import APIRouter, Depends

from models import Employee
from dependencies.services import get_employee_service


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
