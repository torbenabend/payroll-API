from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from models.enums.day_type import DayType


class WorkLog(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None

    date: date
    hours_early_shift: float | None = None
    hours_late_shift: float | None = None
    hours_night_shift: float | None = None
    weekday: str
    day_type: DayType
    mission_related_allowance: float | None = None

    updated_by: int
    updated_at: datetime

    employee_id: int
