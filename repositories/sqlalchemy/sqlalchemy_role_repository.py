from typing import Sequence
from sqlalchemy import select
from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.role_repository import RoleRepository
from models import Role, RoleDB


class SqlAlchemyRoleRepository(SqlAlchemyBaseRepository[RoleDB], RoleRepository):
    model = RoleDB
    schema = Role

    def get_role_names(self) -> Sequence[str]:
        stmt = select(RoleDB.role_name)
        return self.session.execute(stmt).scalars().all()
