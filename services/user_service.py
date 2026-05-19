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
    ):
        new_user = User(
            username=username,
            password=password,
            role_id=role_id,
            employee_id=employee_id
        )
        return self.repository.add(new_user)
    