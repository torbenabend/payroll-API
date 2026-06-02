from datetime import date
from fastapi import APIRouter, Depends

from services import EmployeeService
from dependencies import get_sqlalchemy_employee_repository


router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/active_employees")
def list_active_employees(
        expiry_date: date,
        repo = Depends(get_sqlalchemy_employee_repository)
):
    service = EmployeeService(repo)
    return service.list_active_employees(expiry_date)
