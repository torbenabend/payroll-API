from .base_repository import BaseRepository
from models import Employee, EmployeeDB

class EmployeeRepository(BaseRepository[Employee]):
    model = EmployeeDB
    schema = Employee
