from typing import List

from repositories.worklog_repository import WorkLogRepository
from models.schemas.worklog import WorkLog


class WorkLogService:
    def __init__(self, repository: WorkLogRepository):
        self.repository = repository
        
    def create_worklog(self, new_worklog: WorkLog) -> WorkLog:
        return self.repository.add(new_worklog)

    def delete_worklog(self, worklog_id) -> WorkLog:
        return self.repository.delete(worklog_id)

    def get_worklog(self, worklog_id) -> WorkLog:
        return self.repository.get_by_id(worklog_id)

    def list_worklogs(self) -> List[WorkLog]:
        return self.repository.get_entities()

    def update_worklog(self, worklog: WorkLog):
        return self.repository.update(worklog)
