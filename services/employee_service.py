from datetime import date
from typing import List

from repositories.employee_repository import EmployeeRepository
from models.schemas.employee import Employee
from models.schemas.employee_contract_info import EmployeeContractInfo


class EmployeeService:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def create_employee(self, new_employee: Employee) -> Employee:
        return self.repository.add(new_employee)

    def delete_employee(self, employee_id: int) -> Employee:
        return self.repository.delete(employee_id)

    def get_employee(self, employee_id: int) -> Employee:
        return self.repository.get_by_id(employee_id)

    def list_employees(self) -> List[Employee]:
        return self.repository.get_entities()

    def update_employee(self, employee: Employee) -> Employee:
        return self.repository.update(employee)

    def list_active_employees(
            self,
            expiry_date: date
    ) -> List[EmployeeContractInfo]:
        return self.repository.get_active_employees(expiry_date)

