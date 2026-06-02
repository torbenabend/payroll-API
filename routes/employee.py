from datetime import date
from fastapi import APIRouter, Depends

from dependencies.services import get_employee_service


router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/active_employees")
def list_active_employees(
        expiry_date: date,
        service = Depends(get_employee_service)
):
    return service.list_active_employees(expiry_date)


@router.get("/employees")
def list_employees(service = Depends(get_employee_service)):
    return service.list_employees()
