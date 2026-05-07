from .base_repository import BaseRepository
from models import WorkLog

class WorkLogRepository(BaseRepository[WorkLog]):
    model = WorkLog