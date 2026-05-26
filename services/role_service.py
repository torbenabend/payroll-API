from typing import List
from models import Role
from repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository


    def create_role(
            self,
            role_name: str,
            read_employee_data: bool,
            edit_employee_data: bool,
            process_payroll: bool
    ) -> Role:
        new_role = Role(
            role_name=role_name,
            read_employee_data=read_employee_data,
            edit_employee_data=edit_employee_data,
            process_payroll=process_payroll
        )
        return self.repository.add(new_role)


    def list_roles(self) -> List[Role]:
        return self.repository.get_entities()


    def update_role(
            self,
            role_id: int,
            role_name: str,
            read_employee_data: bool,
            edit_employee_data: bool,
            process_payroll: bool
    ) -> Role:
        updated_role = self.repository.get_by_id(role_id)
        updated_role.role_name = role_name
        updated_role.read_employee_data = read_employee_data
        updated_role.edit_employee_data = edit_employee_data
        updated_role.process_payroll = process_payroll
        return self.repository.update(updated_role)


    def delete_role(self, role_id: int) -> Role:
        return self.repository.delete(role_id)
