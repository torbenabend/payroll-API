import pytest
from unittest.mock import Mock

from services.role_service import RoleService
from models import Role


@pytest.fixture
def repository():
    return Mock()


@pytest.fixture
def service(repository):
    return RoleService(repository)


@pytest.fixture
def default_role():
    return Role(
        id = 1, role_name="Admin", read_employee_data=True,
        edit_employee_data=True, process_payroll=True
    )


def test_create_role(repository, service, default_role):
    repository.add.return_value = default_role

    result = service.create_role(default_role)

    assert result.role_name == "Admin"
    assert result.read_employee_data == True
    repository.add.assert_called_once()


def test_list_roles(service, repository,default_role):
    roles = [default_role]

    repository.get_entities.return_value = roles

    result = service.list_roles()

    assert result == roles
    repository.get_entities.assert_called_once()


def test_update_role(service, repository, default_role):
    repository.update.return_value = default_role

    result = service.update_role(default_role)

    assert result.role_name == "Admin"
    assert result.read_employee_data == True

    repository.update.assert_called_once_with(default_role)


def test_delete_role(repository, service, default_role):
    deleted_role = default_role
    repository.delete.return_value = deleted_role

    result = service.delete_role(1)

    assert result == deleted_role
    repository.delete.assert_called_once_with(1)


def test_get_role(repository, service, default_role):
    repository.get_by_id.return_value = default_role

    result = service.get_role(1)

    assert result == default_role
    repository.get_by_id.assert_called_once_with(1)
