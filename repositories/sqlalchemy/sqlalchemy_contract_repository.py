from typing import List

from sqlalchemy import select
from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.contract_repository import ContractRepository
from models import Contract, ContractDB


class SqlAlchemyContractRepository(
    SqlAlchemyBaseRepository[ContractDB], ContractRepository
):
    model = ContractDB
    schema = Contract

    def get_contracts_by_employee_id(self, employee_id: int) -> List[Contract]:
        stmt = select(ContractDB).where(ContractDB.employee_id == employee_id)
        rows = self.session.execute(stmt).scalars().all()
        if rows:
            return [Contract.model_validate(row) for row in rows]
        return []
