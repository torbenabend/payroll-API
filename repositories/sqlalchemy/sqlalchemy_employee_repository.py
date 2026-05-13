from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.employee_repository import EmployeeRepository
from models import Employee, EmployeeDB


class SqlAlchemyEmployeeRepository(
    SqlAlchemyBaseRepository[EmployeeDB], EmployeeRepository
):
    model = EmployeeDB
    schema = Employee