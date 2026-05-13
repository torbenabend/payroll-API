from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.user_repository import UserRepository
from models import User, UserDB


class SqlAlchemyUserRepository(
    SqlAlchemyBaseRepository[UserDB], UserRepository
):
    model = UserDB
    schema = User