import pytest
from datetime import date

from pydantic import ValidationError

from models import WorkLog
from models.enums.day_type import DayType


@pytest.fixture
def valid_test_data() -> dict:
    return {
        "date": "01/05/2026",
        "hours_early_shift": 8.0,
        "weekday": "Sunday",
        "employee_id": 10
    }


class FakeWorkLog:
    def __init__(self):
        self.id = 2
        self.date = "01/05/2026"
        self.hours_early_shift = 8.0
        self.weekday = "Sunday"
        self.employee_id = 10


def test_worklog_creation_assigns_fields_and_default_values(valid_test_data):
    worklog = WorkLog(**valid_test_data)

    assert worklog.date.year == 2026
    assert worklog.hours_early_shift == 8.0
    assert worklog.weekday == "Sunday"
    assert worklog.employee_id == 10
    assert worklog.hours_late_shift is None
    assert worklog.day_type is None


def test_worklog_missing_fields():
    data = {"date": "01/01/2024"}
    with pytest.raises(ValidationError):
        WorkLog(**data)


def test_worklog_wrong_type(valid_test_data):
    valid_test_data["hours_early_shift"] = "not-a-float"
    with pytest.raises(ValidationError):
        WorkLog(**valid_test_data)


def test_worklog_parse_dates(valid_test_data):
    worklog = WorkLog(**valid_test_data)

    assert isinstance(worklog.date, date)


def test_worklog_invalid_date(valid_test_data):
    valid_test_data["date"] = "not-a-date"
    with pytest.raises(ValidationError):
        WorkLog(**valid_test_data)


def test_worklog_enum_day_type(valid_test_data):
    valid_test_data["day_type"] = DayType.SICK
    worklog = WorkLog(**valid_test_data)

    assert worklog.day_type == DayType.SICK


def test_worklog_enum_wrong_day_type(valid_test_data):
    valid_test_data["day_type"] = "not-a-valid-day-type"
    with pytest.raises(ValidationError):
        WorkLog(**valid_test_data)


def test_worklog_from_attributes():
    fake_worklog = FakeWorkLog()
    worklog = WorkLog.model_validate(fake_worklog)

    assert worklog.date.year == 2026
    assert worklog.hours_early_shift == 8.0
    assert worklog.weekday == "Sunday"
    assert worklog.employee_id == 10
    assert worklog.hours_late_shift is None
    assert worklog.day_type is None
