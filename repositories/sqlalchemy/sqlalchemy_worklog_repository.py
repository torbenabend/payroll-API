from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.worklog_repository import WorkLogRepository
from models import WorkLog, WorkLogDB


class SqlAlchemyWorkLogDBRepository(
    SqlAlchemyBaseRepository[WorkLogDB], WorkLogRepository
):
    model = WorkLogDB
    schema = WorkLog