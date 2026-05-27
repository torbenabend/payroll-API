import pytest
from unittest.mock import Mock
from datetime import date

from services.worklog_service import WorkLogService
from models import WorkLog
from models.enums.day_type import DayType


@pytest.fixture
def repository():
    return Mock()


@pytest.fixture
def service(repository):
    return WorkLogService(repository)


@pytest.fixture
def default_worklog():
    return WorkLog(
        id = 1, date=date(2026,5,1), hours_early_shift=8.0,
        hours_late_shift=None, hours_night_shift=None, weekday="Sunday",
        day_type=None, mission_related_allowance=0.0, employee_id=5
    )


def test_create_worklog(repository, service, default_worklog):
    repository.add.return_value = default_worklog

    result = service.create_worklog(
        work_date=date(2026, 5, 1), hours_early_shift=8.0,
        hours_late_shift=None, hours_night_shift=None, weekday="Sunday",
        day_type=None, mission_related_allowance=0.0, employee_id=5
    )

    assert result.date.year == 2026
    assert result.hours_early_shift == 8.0
    assert result.hours_late_shift is None
    assert result.employee_id == 5
