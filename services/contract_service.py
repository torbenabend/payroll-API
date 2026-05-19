from datetime import date

from models import Contract
from models.enums.salary_type import SalaryType
from repositories.contract_repository import ContractRepository

class ContractService:
    def __init__(self, repository: ContractRepository):
        self.repository = repository

    def create_contract(
            self,
            contract_start: date,
            contract_end: date | None,
            salary_type: SalaryType,
            fixed_salary: float | None,
            hourly_rate: float | None,
            employee_id: int
    ) -> Contract:
        new_contract = Contract(
            contract_start=contract_start,
            contract_end=contract_end,
            salary_type=salary_type,
            fixed_salary=fixed_salary,
            hourly_rate=hourly_rate,
            employee_id=employee_id
        )
        return self.repository.add(new_contract)

    def delete_contract(self, contract_id: int) -> Contract:
        return self.repository.delete(contract_id)

    def get_contract(self, contract_id: int) -> Contract:
        return self.repository.get_by_id(contract_id)
