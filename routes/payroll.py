from datetime import date
from fastapi import APIRouter, Depends, HTTPException

from models import PayrollReport
from dependencies.services import get_payroll_service


router = APIRouter(prefix="/payroll", tags=["Payroll"])

@router.get("/{employee_id}/{year}/{month}")
def process_employee_payroll(
        employee_id: int,
        year: int,
        month: int,
        service = Depends(get_payroll_service)
):
    return service.generate_payroll_report(employee_id, month, year)