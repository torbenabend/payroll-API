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


def test_create_user(repository, service, default_user):
    repository.add.return_value = default_user

    result = service.create_user(default_user)

    assert result.username == "jdoe"
    assert result.role_id == 2
    assert result.employee_id is None


def test_delete_user(repository, service, default_user):
    repository.delete.return_value = default_user

    result = service.delete_user(1)

    assert result == default_user
    repository.delete.assert_called_once_with(1)


def test_get_user(repository, service, default_user):
    repository.get_by_id.return_value = default_user

    result = service.get_user(1)

    assert result == default_user
    repository.get_by_id.assert_called_once_with(1)


def test_list_users(service, repository,default_user):
    users = [default_user]

    repository.get_entities.return_value = users

    result = service.list_users()

    assert result == users
    repository.get_entities.assert_called_once()


def test_update_user(service, repository, default_user):
    repository.update.return_value = default_user

    result = service.update_user(default_user)

    assert result.role_id == 2
    repository.update.assert_called_once_with(default_user)
