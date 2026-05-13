from datetime import date

from pydantic import BaseModel, ConfigDict

from models.enums.salary_type import SalaryType


class Contract(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None

    contract_start: date
    contract_end: date | None = None
    salary_type: SalaryType
    fixed_salary: float | None = None
    hourly_rate: float | None = None
