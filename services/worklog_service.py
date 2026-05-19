from datetime import date, datetime

from models.enums.day_type import DayType
from repositories.worklog_repository import WorkLogRepository
from models.schemas.worklog import WorkLog


class WorkLogService:
    def __init__(self, repository: WorkLogRepository):
        self.repository = repository
        
    def create_worklog(
            self,
            work_date: date,
            hours_early_shift: float,
            hours_late_shift: float,
            hours_night_shift: float,
            weekday: str,
            day_type: DayType | None,
            mission_related_allowance: float,
            employee_id: int
    ) -> WorkLog:
        new_worklog = WorkLog(
            date=work_date,
            hours_early_shift=hours_early_shift,
            hours_late_shift=hours_late_shift,
            hours_night_shift=hours_night_shift,
            weekday=weekday,
            day_type=day_type,
            mission_related_allowance=mission_related_allowance,
            employee_id=employee_id
        )
        return self.repository.add(new_worklog)