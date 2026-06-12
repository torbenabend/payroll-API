from sqlalchemy import select

from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.user_repository import UserRepository
from models import User, UserDB


class SqlAlchemyUserRepository(
    SqlAlchemyBaseRepository[UserDB], UserRepository
):
    model = UserDB
    schema = User

    def get_user_by_username(self, username: str) -> User | None:
        stmt = select(self.model).where(UserDB.username == username)
        result = self.session.execute(stmt).scalars().first()
        if result:
            return User.model_validate(result)
        return None
