from typing import Annotated
from fastapi import APIRouter, Depends

from models import User
from dependencies.services import get_payroll_service
from dependencies.authentification import get_current_user


router = APIRouter(prefix="/payroll", tags=["Payroll"])

@router.get("/{employee_id}/{year}/{month}")
def process_employee_payroll(
        employee_id: int,
        year: int,
        month: int,
        _: Annotated[User, Depends(get_current_user)],
        service = Depends(get_payroll_service)
):
    return service.generate_payroll_report(employee_id, month, year)