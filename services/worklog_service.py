from datetime import date
from typing import List

from models.enums.day_type import DayType
from repositories.worklog_repository import WorkLogRepository
from models.schemas.worklog import WorkLog


class WorkLogService:
    def __init__(self, repository: WorkLogRepository):
        self.repository = repository
        
    def create_worklog(
            self,
            work_date: date,
            hours_early_shift: float | None,
            hours_late_shift: float | None,
            hours_night_shift: float | None,
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

    def delete_worklog(self, worklog_id) -> WorkLog:
        return self.repository.delete(worklog_id)

    def get_worklog(self, worklog_id) -> WorkLog:
        return self.repository.get_by_id(worklog_id)

    def list_worklogs(self) -> List[WorkLog]:
        return self.repository.get_entities()

    def update_worklog(
            self,
            worklog_id: int,
            work_date: date,
            hours_early_shift: float | None,
            hours_late_shift: float | None,
            hours_night_shift: float | None,
            weekday: str,
            day_type: DayType | None,
            mission_related_allowance: float,
            employee_id: int
    ):
        updated_worklog = self.repository.get_by_id(worklog_id)
        updated_worklog.date = work_date
        updated_worklog.hours_early_shift = hours_early_shift
        updated_worklog.hours_late_shift = hours_late_shift
        updated_worklog.hours_night_shift = hours_night_shift
        updated_worklog.weekday = weekday
        updated_worklog.day_type = day_type
        updated_worklog.mission_related_allowance = mission_related_allowance
        updated_worklog.employee_id = employee_id
        return self.repository.update(updated_worklog)
