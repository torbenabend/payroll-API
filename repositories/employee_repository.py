from .base_repository import BaseRepository
from models import Employee

class EmployeeRepository(BaseRepository[Employee]):
    model = Employee