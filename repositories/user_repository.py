from abc import abstractmethod

from .base_repository import BaseRepository
from models import User, UserDB, Role

class UserRepository(BaseRepository[User]):
    model = UserDB
    schema = User

    @abstractmethod
    def get_user_by_username(self, username: str) -> User | None:
        pass

    @abstractmethod
    def get_user_role(self, user_id: int) -> Role | None:
        pass
