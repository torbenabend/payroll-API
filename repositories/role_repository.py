from abc import abstractmethod
from typing import List
from .base_repository import BaseRepository
from models import Role

class RoleRepository(BaseRepository[Role]):
    model = Role

    @abstractmethod
    def get_role_names(self) -> List[Role]:
        pass
