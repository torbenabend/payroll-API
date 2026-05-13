from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.contract_repository import ContractRepository
from models import Contract, ContractDB


class SqlAlchemyContractRepository(
    SqlAlchemyBaseRepository[ContractDB], ContractRepository
):
    model = ContractDB
    schema = Contract