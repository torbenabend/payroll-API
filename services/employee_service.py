from datetime import date, datetime
from typing import List

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

    def delete_employee(self, employee_id: int) -> Employee:
        return self.repository.delete(employee_id)

    def get_employee(self, employee_id: int) -> Employee:
        return self.repository.get_by_id(employee_id)

    def list_employees(self) -> List[Employee]:
        return self.repository.get_entities()

    def update_employee(
            self,
            employee_id: int,
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
        updated_employee = self.repository.get_by_id(employee_id)
        updated_employee.last_name=last_name
        updated_employee.first_name=first_name
        updated_employee.birth_date=birth_date
        updated_employee.tax_id=tax_id
        updated_employee.social_security_number=social_security_number
        updated_employee.street_name=street_name
        updated_employee.house_number=house_number
        updated_employee.postal_code=postal_code
        updated_employee.city=city
        updated_employee.tax_class=tax_class
        updated_employee.child_allowance=child_allowance
        updated_employee.denomination=denomination
        updated_employee.work_permit_end=work_permit_end
        updated_employee.residence_permit_end=residence_permit_end
        updated_employee.payment_method=payment_method
        updated_employee.iban=iban
        return self.repository.update(updated_employee)
