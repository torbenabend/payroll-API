from sqlalchemy import select

from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.user_repository import UserRepository
from models import User, UserDB, Role


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

    def get_user_role(self, user_id: int) -> Role | None:
        stmt = select(self.model).where(UserDB.id == user_id)
        result = self.session.execute(stmt).scalars().first()
        return Role.model_validate(result.role)
        #user = self.get_by_id(user_id)
        #if user:
        #    return Role.model_validate(user.role)
        #return None
