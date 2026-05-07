from fastapi import FastAPI, Depends
from dependencies import get_sqlalchemy_role_repository
from services import RoleService
app = FastAPI()


@app.get("/roles")
def list_roles(repo = Depends(get_sqlalchemy_role_repository)):
    service = RoleService(repo)
    return service.list_roles()

@app.post("/roles")
def create_role(
        role_name: str,
        read_employee_data: bool,
        edit_employee_data: bool,
        process_payroll: bool,
        repo = Depends(get_sqlalchemy_role_repository)
):
    service = RoleService(repo)
    return service.create_role(
        role_name=role_name,
        read_employee_data=read_employee_data,
        edit_employee_data=edit_employee_data,
        process_payroll=process_payroll
    )


@app.put("/roles/{role_id}")
def update_role(
        role_id: int,
        role_name: str,
        read_employee_data: bool,
        edit_employee_data: bool,
        process_payroll: bool,
        repo = Depends(get_sqlalchemy_role_repository)
):
    service = RoleService(repo)
    return service.update_role(
        role_id=role_id,
        role_name= role_name,
        read_employee_data=read_employee_data,
        edit_employee_data=edit_employee_data,
        process_payroll=process_payroll
    )


@app.delete("/roles/{role_id}")
def delete_role(role_id, repo = Depends(get_sqlalchemy_role_repository)):
    service = RoleService(repo)
    return service.delete_role(role_id)
