from abc import abstractmethod

from .base_repository import BaseRepository
from models import User, UserDB

class UserRepository(BaseRepository[User]):
    model = UserDB
    schema = User

    @abstractmethod
    def get_user_by_username(self, username: str) -> User | None:
        pass