from .base_repository import BaseRepository
from models import Contract

class ContractRepository(BaseRepository[Contract]):
    model = Contract