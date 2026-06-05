from abc import abstractmethod
from typing import List

from .base_repository import BaseRepository
from models import WorkLog, WorkLogDB


class WorkLogRepository(BaseRepository[WorkLog]):
    model = WorkLogDB
    schema = WorkLog

    @abstractmethod
    def get_worklogs_by_employee_id_and_month(
            self,
            employee_id: int,
            month: int,
            year: int
    ) -> List[WorkLog]:
        pass