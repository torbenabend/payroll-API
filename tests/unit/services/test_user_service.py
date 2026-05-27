import pytest
from unittest.mock import Mock

from services.user_service import UserService
from models import User


@pytest.fixture
def repository():
    return Mock()


@pytest.fixture
def service(repository):
    return UserService(repository)


@pytest.fixture
def default_user():
    return User(
        id = 1, username="jdoe", password="******", role_id=2, employee_id=None
    )


def test_create_employee(repository, service, default_user):
    repository.add.return_value = default_user

    result = service.create_user(
        username="jdoe", password="******", role_id=2, employee_id=None
    )

    assert result.username == "jdoe"
    assert result.role_id == 2
    assert result.employee_id is None
