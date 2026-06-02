from abc import abstractmethod
from datetime import date
from typing import List

from .base_repository import BaseRepository
from models import Employee, EmployeeDB
from models.schemas.employee_contract_info import EmployeeContractInfo

class EmployeeRepository(BaseRepository[Employee]):
    model = EmployeeDB
    schema = Employee

    @abstractmethod
    def get_active_employees(
            self,
            expiry_date: date
    ) -> List[EmployeeContractInfo]:
        pass
