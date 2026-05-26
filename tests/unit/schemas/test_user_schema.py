import pytest

from pydantic import ValidationError

from models import User


@pytest.fixture
def valid_test_data() -> dict:
    return {
        "username": "johndoe",
        "password": 8 * "*",
        "role_id": 2
    }


class FakeUser:
    def __init__(self):
        self.id = 3
        self.username = "johndoe"
        self.password = 8 * "*"
        self.role_id = 2
        self.employee_id = 4


def test_user_creation_assigns_fields_and_default_id(valid_test_data):
    user = User(**valid_test_data)

    assert user.username == "johndoe"
    assert user.role_id == 2
    assert user.id is None


def test_user_missing_fields():
    data = {"username": "johndoe"}
    with pytest.raises(ValidationError):
        User(**data)


def test_user_wrong_type(valid_test_data):
    valid_test_data["password"] = 123
    with pytest.raises(ValidationError):
        User(**valid_test_data)


def test_user_from_attributes():
    fake_user = FakeUser()
    user = User.model_validate(fake_user)

    assert user.id == 3
    assert user.username == "johndoe"
    assert user.employee_id == 4
