from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.employee_repository import EmployeeRepository
from models import Employee


class SqlAlchemyEmployeeRepository(
    SqlAlchemyBaseRepository[Employee], EmployeeRepository
):
    model = Employee