from typing import List

from models import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, new_user: User) -> User:
        return self.repository.add(new_user)

    def delete_user(self, user_id) -> User:
        return self.repository.delete(user_id)

    def get_user(self, user_id) -> User:
        return self.repository.get_by_id(user_id)

    def list_users(self) -> List[User]:
        return self.repository.get_entities()

    def update_user(self, user: User) -> User:
        return self.repository.update(user)
