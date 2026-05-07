from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.worklog_repository import WorkLogRepository
from models import WorkLog


class SqlAlchemyWorkLogRepository(
    SqlAlchemyBaseRepository[WorkLog], WorkLogRepository
):
    model = WorkLog