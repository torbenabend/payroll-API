from fastapi import Depends

from dependencies.repositories import (
    get_sqlalchemy_employee_repository,
    get_sqlalchemy_role_repository,
    get_sqlalchemy_user_repository,
    get_sqlalchemy_worklog_repository,
    get_sqlalchemy_contract_repository
)
from services import (
    EmployeeService,
    RoleService,
    UserService,
    WorkLogService,
    ContractService
)


def get_employee_service(repo = Depends(get_sqlalchemy_employee_repository)):
    return EmployeeService(repo)


def get_role_service(repo = Depends(get_sqlalchemy_role_repository)):
    return RoleService(repo)


def get_user_service(repo = Depends(get_sqlalchemy_user_repository)):
    return UserService(repo)


def get_worklog_service(repo = Depends(get_sqlalchemy_worklog_repository)):
    return WorkLogService(repo)


def get_contract_service(repo = Depends(get_sqlalchemy_contract_repository)):
    return ContractService(repo)
