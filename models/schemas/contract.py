from datetime import date
from typing import Annotated

from pydantic import BaseModel, ConfigDict, BeforeValidator

from models.enums.salary_type import SalaryType
from models.validators.common import parse_date


class Contract(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None

    contract_start: Annotated[date, BeforeValidator(parse_date)]
    contract_end: Annotated[date | None, BeforeValidator(parse_date)] = None
    salary_type: SalaryType
    fixed_salary: float | None = None
    hourly_rate: float | None = None
