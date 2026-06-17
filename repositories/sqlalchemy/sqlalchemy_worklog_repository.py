from typing import List

from sqlalchemy import select, extract
from .sqlalchemy_base_repository import SqlAlchemyBaseRepository
from repositories.worklog_repository import WorkLogRepository
from models import WorkLog, WorkLogDB


class SqlAlchemyWorkLogRepository(
    SqlAlchemyBaseRepository[WorkLogDB], WorkLogRepository
):
    model = WorkLogDB
    schema = WorkLog

    def get_worklogs_by_employee_id_and_month(
            self,
            employee_id: int,
            month: int,
            year: int
    ) -> List[WorkLog]:
        stmt = select(WorkLogDB).where(
            WorkLogDB.employee_id == employee_id,
            extract("month", WorkLogDB.date) == month,
            extract("year", WorkLogDB.date) == year
        )
        rows = self.session.execute(stmt).scalars().all()
        if rows:
            return [self.schema.model_validate(row) for row in rows]
        return []
