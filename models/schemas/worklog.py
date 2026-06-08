from datetime import date
from typing import Annotated

from pydantic import BaseModel, ConfigDict, BeforeValidator

from constants import DEFAULT_HOURS, SUNDAY_STR
from models.enums.day_type import DayType
from models.schemas.payroll_report import WorkingHours
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


    @property
    def daily_working_hours(self):
        return (self.hours_early_shift
                + self.hours_late_shift
                + self.hours_night_shift)


    def apply_to(self, working_hours: WorkingHours):
        if self.day_type == DayType.HOLIDAY:
            working_hours.holiday += self.daily_working_hours
            return

        if self.day_type == DayType.SICK:
            working_hours.sick += DEFAULT_HOURS
            return

        if self.day_type == DayType.VACATION:
            working_hours.vacation += DEFAULT_HOURS
            return

        if self.day_type == DayType.HOLIDAY_PAYED:
            working_hours.holiday_pay += DEFAULT_HOURS
            return

        if self.weekday == SUNDAY_STR:
            working_hours.sunday += self.daily_working_hours
            return

        working_hours.early_shift += self.hours_early_shift
        working_hours.late_shift += self.hours_late_shift
        working_hours.night_shift += self.hours_night_shift
