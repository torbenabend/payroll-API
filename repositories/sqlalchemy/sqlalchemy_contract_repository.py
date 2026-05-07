from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.contract_repository import ContractRepository
from models import Contract


class SqlAlchemyContractRepository(
    SqlAlchemyBaseRepository[Contract], ContractRepository
):
    model = Contract