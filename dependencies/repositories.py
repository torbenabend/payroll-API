from fastapi import Depends

from repositories.sqlalchemy.sqlalchemy_role_repository import SqlAlchemyRoleRepository
from repositories.sqlalchemy.sqlalchemy_contract_repository import SqlAlchemyContractRepository
from repositories.sqlalchemy.sqlalchemy_employee_repository import SqlAlchemyEmployeeRepository
from repositories.sqlalchemy.sqlalchemy_user_repository import SqlAlchemyUserRepository
from repositories.sqlalchemy.sqlalchemy_worklog_repository import SqlAlchemyWorkLogRepository
from dependencies.db import get_db


def get_sqlalchemy_role_repository(db = Depends(get_db)):
    return SqlAlchemyRoleRepository(db)


def get_sqlalchemy_employee_repository(db = Depends(get_db)):
    return SqlAlchemyEmployeeRepository(db)


def get_sqlalchemy_contract_repository(db = Depends(get_db)):
    return SqlAlchemyContractRepository(db)


def get_sqlalchemy_user_repository(db = Depends(get_db)):
    return SqlAlchemyUserRepository(db)


def get_sqlalchemy_worklog_repository(db = Depends(get_db)):
    return SqlAlchemyWorkLogRepository(db)
