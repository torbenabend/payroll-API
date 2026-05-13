from pydantic import BaseModel, ConfigDict


class Role(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None

    role_name: str
    read_employee_data: bool
    edit_employee_data: bool
    process_payroll: bool
