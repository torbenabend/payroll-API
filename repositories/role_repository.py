from abc import abstractmethod
from typing import List
from .base_repository import BaseRepository
from models import Role, RoleDB

class RoleRepository(BaseRepository[Role]):
    model = RoleDB
    schema = Role

    @abstractmethod
    def get_role_names(self) -> List[Role]:
        pass
