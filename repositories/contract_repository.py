from abc import abstractmethod
from typing import List

from .base_repository import BaseRepository
from models import Contract, ContractDB

class ContractRepository(BaseRepository[Contract]):
    model = ContractDB
    schema = Contract

    @abstractmethod
    def get_contracts_by_employee_id(self, employee_id: int) -> List[Contract]:
        pass

    @abstractmethod
    def get_active_contract(
            self,
            employee_id: int,
            month: int,
            year: int
    ) -> Contract | None:
        pass
