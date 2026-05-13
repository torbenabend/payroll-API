from .base_repository import BaseRepository
from models import WorkLog, WorkLogDB

class WorkLogRepository(BaseRepository[WorkLog]):
    model = WorkLogDB
    schema = WorkLog