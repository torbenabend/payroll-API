from pathlib import Path
from typing import List, Dict
import json

from services.role_service import RoleService
from repositories.sqlalchemy.sqlalchemy_role_repository import \
    SqlAlchemyRoleRepository
from services.employee_service import EmployeeService
from repositories.sqlalchemy.sqlalchemy_employee_repository import \
    SqlAlchemyEmployeeRepository
from services.user_service import UserService
from repositories.sqlalchemy.sqlalchemy_user_repository import \
    SqlAlchemyUserRepository
from services.worklog_service import WorkLogService
from repositories.sqlalchemy.sqlalchemy_worklog_repository import \
    SqlAlchemyWorkLogRepository
from services.contract_service import ContractService
from repositories.sqlalchemy.sqlalchemy_contract_repository import \
    SqlAlchemyContractRepository
from db.database import Session, engine, Base


def import_data(file_name: str) -> List[Dict]:
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "data" / "examples" / file_name
    with open(file_path,"r", encoding="utf-8") as file:
        return json.load(file)


def create_demo_roles():
    roles = import_data("roles_example_data.json")
    repo = SqlAlchemyRoleRepository(Session())
    service = RoleService(repo)
    for role in roles:
        service.create_role(**role)


def create_demo_employees():
    employees = import_data("employees_example_data.json")
    repo = SqlAlchemyEmployeeRepository(Session())
    service = EmployeeService(repo)

    for employee in employees:
        service.create_employee(**employee)


def create_demo_admin_user():
    admin_user = import_data("admin_user_example_data.json")
    repo = SqlAlchemyUserRepository(Session())
    service = UserService(repo)

    for user in admin_user:
        service.create_user(**user)


def create_demo_users():
    users = import_data("user_example_data.json")
    repo = SqlAlchemyUserRepository(Session())
    service = UserService(repo)

    for user in users:
        service.create_user(**user)


def create_demo_worklogs():
    worklogs = import_data("worklogs_example_data.json")
    repo= SqlAlchemyWorkLogRepository(Session())
    service = WorkLogService(repo)

    for worklog in worklogs:
        service.create_worklog(**worklog)


def create_demo_contracts():
    contracts = import_data("contracts_example_data.json")
    repo = SqlAlchemyContractRepository(Session())
    service = ContractService(repo)

    for contract in contracts:
        service.create_contract(**contract)


def seed_db():
    create_demo_roles()
    create_demo_admin_user()
    create_demo_employees()
    create_demo_users()
    create_demo_worklogs()
    create_demo_contracts()


if __name__ == "__main__":
    seed_db()
