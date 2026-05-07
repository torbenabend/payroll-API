from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.user_repository import UserRepository
from models import User


class SqlAlchemyUserRepository(
    SqlAlchemyBaseRepository[User], UserRepository
):
    model = User