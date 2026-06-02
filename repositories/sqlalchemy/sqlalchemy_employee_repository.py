from datetime import date
from typing import List

from sqlalchemy import select, or_
from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.employee_repository import EmployeeRepository
from models import Employee, EmployeeDB, ContractDB
from models.schemas.employee_contract_info import EmployeeContractInfo


class SqlAlchemyEmployeeRepository(
    SqlAlchemyBaseRepository[EmployeeDB], EmployeeRepository
):
    model = EmployeeDB
    schema = Employee

    def get_active_employees(
            self,
            expiry_date: date
    ) -> List[EmployeeContractInfo]:
        stmt = (
            select(
                EmployeeDB.last_name,
                EmployeeDB.first_name,
                ContractDB.contract_end)
            .join(EmployeeDB.contracts)
            .where(
                or_(
                    ContractDB.contract_end >= expiry_date,
                    ContractDB.contract_end.is_(None)
                )
            )
        )
        rows = self.session.execute(stmt).mappings().all()
        return [EmployeeContractInfo(**row) for row in rows]
