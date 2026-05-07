from db.database import Session
from repositories.sqlalchemy.sqlalchemy_role_repository import SqlAlchemyRoleRepository
from repositories.sqlalchemy.sqlalchemy_contract_repository import SqlAlchemyContractRepository

def get_sqlalchemy_role_repository():
    return SqlAlchemyRoleRepository(Session())
