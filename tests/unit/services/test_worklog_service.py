import pytest
from unittest.mock import Mock
from datetime import date

from services.worklog_service import WorkLogService
from models import WorkLog


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

    result = service.create_worklog(default_worklog)

    assert result.date.year == 2026
    assert result.hours_early_shift == 8.0
    assert result.hours_late_shift is None
    assert result.employee_id == 5


def test_list_worklogs(service, repository,default_worklog):
    worklogs = [default_worklog]

    repository.get_entities.return_value = worklogs

    result = service.list_worklogs()

    assert result == worklogs
    repository.get_entities.assert_called_once()


def test_update_worklog(service, repository, default_worklog):
    repository.update.return_value = default_worklog

    result = service.update_worklog(default_worklog)

    assert result.hours_early_shift == 8.0
    assert result.hours_late_shift is None
    assert result.mission_related_allowance == 0.0

    repository.update.assert_called_once_with(default_worklog)


def test_delete_worklog(repository, service, default_worklog):
    deleted_worklog = default_worklog
    repository.delete.return_value = deleted_worklog

    result = service.delete_worklog(1)

    assert result == deleted_worklog
    repository.delete.assert_called_once_with(1)


def test_get_worklog(repository, service, default_worklog):
    repository.get_by_id.return_value = default_worklog

    result = service.get_worklog(1)

    assert result == default_worklog
    repository.get_by_id.assert_called_once_with(1)
