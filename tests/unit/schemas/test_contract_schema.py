import pytest
from datetime import date

from pydantic import ValidationError

from models import Contract
from models.enums.salary_type import SalaryType


@pytest.fixture
def valid_test_data() -> dict:
    return {
        "contract_start": "01/10/2021",
        "salary_type": SalaryType.SALARY,
        "fixed_salary": 5000,
        "employee_id": 4
    }


class FakeContract:
    def __init__(self):
        self.id = 3
        self.contract_start = "01/10/2021"
        self.salary_type = SalaryType.SALARY
        self.fixed_salary = 5000
        self.employee_id = 4



def test_contract_creation_assigns_fields_and_default_values(valid_test_data):
    contract = Contract(**valid_test_data)

    assert contract.contract_start.year == 2021
    assert contract.contract_end is None
    assert contract.salary_type == SalaryType.SALARY
    assert contract.hourly_rate is None
    assert contract.id is None


def test_contract_missing_fields():
    data = {"contract_start": "01/01/2024"}
    with pytest.raises(ValidationError):
        Contract(**data)


def test_contract_wrong_type(valid_test_data):
    valid_test_data["fixed_salary"] = "not-a-float"
    with pytest.raises(ValidationError):
        Contract(**valid_test_data)


def test_contract_parse_dates(valid_test_data):
    valid_test_data["contract_end"] = "31/12/2026"
    contract = Contract(**valid_test_data)

    assert isinstance(contract.contract_start, date)
    assert isinstance(contract.contract_end, date)


def test_contract_invalid_date(valid_test_data):
    valid_test_data["contract_start"] = "not-a-date"
    with pytest.raises(ValidationError):
        Contract(**valid_test_data)


def test_contract_enum_salary_type(valid_test_data):
    valid_test_data["salary_type"] = "fixed"
    with pytest.raises(ValidationError):
        Contract(**valid_test_data)


def test_contract_from_attributes():
    fake_contract = FakeContract()
    contract = Contract.model_validate(fake_contract)

    assert contract.id == 3
    assert contract.contract_start.year == 2021
    assert contract.salary_type == SalaryType.SALARY
