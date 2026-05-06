from typing import Sequence, Optional
from sqlalchemy import select
from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.role_repository import RoleRepository
from models import Role


class SqlAlchemyRoleRepository(SqlAlchemyBaseRepository[Role], RoleRepository):
    model = Role

    def get_role_names(self) -> Sequence[str]:
        stmt = select(Role.role_name)
        return self.session.execute(stmt).scalars().all()
