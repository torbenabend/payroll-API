from models import Role
from repositories import RoleRepository

class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def create_role(self, role: Role) -> Role:
        return self.repository.add(role)

    def list_role_names(self):
        return self.repository.get_role_names()
