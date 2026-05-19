from datetime import date, datetime

from repositories.employee_repository import EmployeeRepository
from models.schemas.employee import Employee
from models.enums.payment_method import PaymentMethod


class EmployeeService:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def create_employee(
            self,
            last_name: str,
            first_name: str,
            birth_date: date,
            tax_id: str,
            social_security_number: str,
            street_name: str,
            house_number: str,
            postal_code: str,
            city: str,
            tax_class: int,
            child_allowance: float,
            denomination: str,
            work_permit_end: date | None,
            residence_permit_end: date | None,
            payment_method: PaymentMethod,
            iban: str | None

    ) -> Employee:
        new_employee = Employee(
            last_name=last_name,
            first_name=first_name,
            birth_date=birth_date,
            tax_id=tax_id,
            social_security_number=social_security_number,
            street_name=street_name,
            house_number=house_number,
            postal_code=postal_code,
            city=city,
            tax_class=tax_class,
            child_allowance=child_allowance,
            denomination=denomination,
            work_permit_end=work_permit_end,
            residence_permit_end=residence_permit_end,
            payment_method=payment_method,
            iban=iban
        )
        return self.repository.add(new_employee)
