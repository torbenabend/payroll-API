from datetime import date
from typing import Annotated

from pydantic import BaseModel, ConfigDict, BeforeValidator

from models.enums.day_type import DayType
from models.validators.common import parse_date


class WorkLog(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None

    date: Annotated[date, BeforeValidator(parse_date)]
    hours_early_shift: float | None = None
    hours_late_shift: float | None = None
    hours_night_shift: float | None = None
    weekday: str
    day_type: DayType | None = None
    mission_related_allowance: float | None = None

    employee_id: int
