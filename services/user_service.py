from typing import List

from models import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(
            self,
            username: str,
            password: str,
            role_id: int,
            employee_id: int | None
    ) -> User:
        new_user = User(
            username=username,
            password=password,
            role_id=role_id,
            employee_id=employee_id
        )
        return self.repository.add(new_user)

    def delete_user(self, user_id) -> User:
        return self.repository.delete(user_id)

    def get_user(self, user_id) -> User:
        return self.repository.get_by_id(user_id)

    def list_users(self) -> List[User]:
        return self.repository.get_entities()

    def update_user(
            self,
            user_id: int,
            username: str,
            password: str,
            role_id: int,
            employee_id: int | None
    ) -> User:
        updated_user = self.repository.get_by_id(user_id)
        updated_user.username = username
        updated_user.password = password
        updated_user.role_id = role_id
        updated_user.employee_id = employee_id
        return self.repository.update(updated_user)
