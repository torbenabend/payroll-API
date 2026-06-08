from typing import List

from repositories.employee_repository import EmployeeRepository
from repositories.contract_repository import ContractRepository
from repositories.worklog_repository import WorkLogRepository
from models import WorkLog
from models.schemas.payroll_report import PayrollReport, EmployeeInfo, Period, WorkingHours, TaxablePay, PremiumPay
from utils.utils import get_business_days_in_month


class PayrollService:
    def __init__(
            self,
            employee_repository: EmployeeRepository,
            contract_repository: ContractRepository,
            worklog_repository: WorkLogRepository
    ):
        self.employee_repository = employee_repository
        self.contract_repository = contract_repository
        self.worklog_repository = worklog_repository

    def generate_payroll_report(
            self,
            employee_id: int,
            month: int,
            year: int
    ):
        employee_info = self._get_employee_info(employee_id)
        period = Period(month=month, year=year)

        hourly_rate = self._get_hourly_rate(employee_id, month, year)
        working_hours = self._calculate_working_hours(employee_id, month, year)
        taxable_pay = TaxablePay(average_wage=1.04)
        taxable_pay.calculate(working_hours, hourly_rate)
        premium_pay = PremiumPay()
        premium_pay.calculate(working_hours, hourly_rate)
        return PayrollReport(
            employee_info=employee_info,
            period=period,
            working_hours=working_hours,
            taxable_pay=taxable_pay,
            premium_pay=premium_pay
        )

    def _get_employee_info(self, employee_id: int) -> EmployeeInfo:
        employee = self.employee_repository.get_by_id(employee_id)
        return EmployeeInfo.model_validate(employee)

    def _get_worklogs(
            self,
            employee_id: int,
            month: int,
            year: int
    ) -> List[WorkLog]:
        return self.worklog_repository.get_worklogs_by_employee_id_and_month(
            employee_id, month, year
        )

    def _get_hourly_rate(self, employee_id, month: int, year: int) -> float:
        active_contract = self.contract_repository.get_active_contract(
            employee_id,
            month,
            year
        )
        return active_contract.hourly_rate

    def _calculate_working_hours(
            self,
            employee_id: int,
            month: int,
            year: int
    ) -> WorkingHours:
        working_hours = WorkingHours()
        for worklog in self._get_worklogs(employee_id, month, year):
            worklog.apply_to(working_hours)
        working_hours.apply_overtime(
            business_days=get_business_days_in_month(month, year)
        )
        return working_hours
