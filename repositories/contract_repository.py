from .base_repository import BaseRepository
from models import Contract, ContractDB

class ContractRepository(BaseRepository[Contract]):
    model = ContractDB
    schema = Contract