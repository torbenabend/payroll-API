from typing import List
from models import Role
from repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def create_role(self, new_role: Role) -> Role:
        return self.repository.add(new_role)

    def list_roles(self) -> List[Role]:
        return self.repository.get_entities()

    def update_role(self, role: Role) -> Role:
        return self.repository.update(role)

    def delete_role(self, role_id: int) -> Role:
        return self.repository.delete(role_id)

    def get_role(self, role_id: int) -> Role:
        return self.repository.get_by_id(role_id)
