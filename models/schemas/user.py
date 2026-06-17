from pydantic import BaseModel, ConfigDict

from models import Role


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None

    username: str
    password: str

    role_id: int
    employee_id: int | None = None

    role: Role
