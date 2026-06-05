from typing import List

from models import Contract
from repositories.contract_repository import ContractRepository

class ContractService:
    def __init__(self, repository: ContractRepository):
        self.repository = repository

    def create_contract(self, new_contract: Contract) -> Contract:
        return self.repository.add(new_contract)

    def delete_contract(self, contract_id: int) -> Contract:
        return self.repository.delete(contract_id)

    def get_contract(self, contract_id: int) -> Contract:
        return self.repository.get_by_id(contract_id)

    def list_contracts(self) -> List[Contract]:
        return self.repository.get_entities()

    def update_contract(self, contract: Contract) -> Contract:
        return self.repository.update(contract)

    def get_employee_contracts(self, employee_id: int) -> List[Contract]:
        return self.repository.get_contracts_by_employee_id(employee_id)
