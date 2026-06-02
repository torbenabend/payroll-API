from db.database import Session
from repositories.sqlalchemy.sqlalchemy_role_repository import SqlAlchemyRoleRepository
from repositories.sqlalchemy.sqlalchemy_contract_repository import SqlAlchemyContractRepository
from repositories.sqlalchemy.sqlalchemy_employee_repository import SqlAlchemyEmployeeRepository
from repositories.sqlalchemy.sqlalchemy_user_repository import SqlAlchemyUserRepository
from repositories.sqlalchemy.sqlalchemy_worklog_repository import SqlAlchemyWorkLogRepository

def get_sqlalchemy_role_repository():
    return SqlAlchemyRoleRepository(Session())


def get_sqlalchemy_employee_repository():
    return SqlAlchemyEmployeeRepository(Session())


def get_sqlalchemy_contract_repository():
    return SqlAlchemyContractRepository(Session())


def get_sqlalchemy_user_repository():
    return SqlAlchemyUserRepository(Session())


def get_sqlalchemy_worklog_repository():
    return SqlAlchemyWorkLogRepository(Session())
