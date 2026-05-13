from .base_repository import BaseRepository
from models import User, UserDB

class UserRepository(BaseRepository[User]):
    model = UserDB
    schema = User