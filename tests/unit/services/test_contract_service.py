import pytest
from unittest.mock import Mock
from datetime import date

from services.contract_service import ContractService
from models import Contract
from models.enums.salary_type import SalaryType


@pytest.fixture
def repository():
    return Mock()


@pytest.fixture
def service(repository):
    return ContractService(repository)


@pytest.fixture
def default_contract():
    return Contract(
        id = 1, contract_start=date(2025,5,1),
        contract_end=None, salary_type=SalaryType.WAGE, fixed_salary=None,
        hourly_rate=25.0, employee_id=5
    )


def test_create_contract(repository, service, default_contract):
    repository.add.return_value = default_contract

    result = service.create_contract(default_contract)

    assert result.contract_start == date(2025,5,1)
    assert result.contract_end is None
    assert result.hourly_rate == 25.0
    repository.add.assert_called_once()


def test_delete_contract(repository, service, default_contract):
    repository.delete.return_value = default_contract

    result = service.delete_contract(1)

    assert result == default_contract
    repository.delete.assert_called_once_with(1)


def test_get_contract(repository, service, default_contract):
    repository.get_by_id.return_value = default_contract

    result = service.get_contract(1)

    assert result == default_contract
    repository.get_by_id.assert_called_once_with(1)


def test_list_contracts(repository, service, default_contract):
    contracts = [default_contract]
    repository.get_entities.return_value = contracts

    result = service.list_contracts()

    assert result == contracts
    repository.get_entities.assert_called_once()


def test_update_contract(service, repository, default_contract):
    repository.update.return_value = default_contract

    result = service.update_contract(default_contract)

    assert result.contract_start.year == 2025
    assert result.salary_type == SalaryType.WAGE
    assert result.fixed_salary is None
    assert result.hourly_rate == 25.0
    repository.update.assert_called_once_with(default_contract)
