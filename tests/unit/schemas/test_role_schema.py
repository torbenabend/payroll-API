import pytest

from pydantic import ValidationError

from models import Role


@pytest.fixture
def valid_test_data() -> dict:
    return {
        "role_name": "HR",
        "read_employee_data": True,
        "edit_employee_data": True,
        "process_payroll": False
    }


class FakeRole:
    def __init__(self):
        self.id = 3
        self.role_name = "admin"
        self.read_employee_data = True
        self.edit_employee_data = True
        self.process_payroll = True


def test_role_creation_assigns_fields_and_default_id(valid_test_data):
    role = Role(**valid_test_data)

    assert role.role_name == "HR"
    assert role.read_employee_data is True
    assert role.edit_employee_data is True
    assert role.process_payroll is False
    assert role.id is None


def test_role_missing_fields():
    data = {"role_name": "admin"}
    with pytest.raises(ValidationError):
        Role(**data)


def test_role_wrong_type(valid_test_data):
    valid_test_data["read_employee_data"] = "not-boolean"
    with pytest.raises(ValidationError):
        Role(**valid_test_data)


def test_role_from_attributes():
    fake_role = FakeRole()
    role = Role.model_validate(fake_role)

    assert role.id == 3
    assert role.role_name == "admin"
    assert role.process_payroll == True
