from typing import List

from sqlalchemy import select, or_
from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.contract_repository import ContractRepository
from models import Contract, ContractDB
from utils.utils import get_month_range


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

    def get_active_contract(
            self,
            employee_id: int,
            month: int,
            year: int
    ) -> Contract | None:
        start, end = get_month_range(month, year)
        stmt = select(ContractDB).where(
            ContractDB.employee_id == employee_id,
            ContractDB.contract_start < end,
            or_(
                ContractDB.contract_end >= start,
                ContractDB.contract_end.is_(None)
            )
        )
        result = self.session.execute(stmt).scalars().first()
        if result:
            return Contract.model_validate(result)
        return None
