import pytest
from unittest.mock import Mock
from datetime import date

from services.employee_service import EmployeeService
from models import Employee
from models.enums.payment_method import PaymentMethod
from models.schemas.employee_contract_info import EmployeeContractInfo


@pytest.fixture
def repository():
    return Mock()


@pytest.fixture
def service(repository):
    return EmployeeService(repository)


@pytest.fixture
def default_employee():
    return Employee(
        id = 1, last_name="Doe", first_name="John", birth_date=date(1980,6,5),
        tax_id="1234", social_security_number="1234",
        street_name="Main Street", house_number="45a", postal_code="5555",
        city="Springfield", tax_class=1, child_allowance=0.0,
        denomination="catholic", work_permit_end=None,
        residence_permit_end=None, payment_method=PaymentMethod.BANK_TRANSFER,
        iban="DE12345678"
    )


def test_create_employee(repository, service, default_employee):
    repository.add.return_value = default_employee

    result = service.create_employee(default_employee)

    assert result.last_name == "Doe"
    assert result.birth_date.year == 1980
    assert result.work_permit_end is None
    assert result.payment_method == PaymentMethod.BANK_TRANSFER


def test_delete_employee(repository, service, default_employee):
    deleted_employee = default_employee
    repository.delete.return_value = deleted_employee

    result = service.delete_employee(1)

    assert result == deleted_employee
    repository.delete.assert_called_once_with(1)


def test_get_employee(repository, service, default_employee):
    repository.get_by_id.return_value = default_employee

    result = service.get_employee(1)

    assert result == default_employee
    repository.get_by_id.assert_called_once_with(1)


def test_list_employees(repository, service, default_employee):
    employees = [default_employee]
    repository.get_entities.return_value = employees

    result = service.list_employees()

    assert result == employees
    repository.get_entities.assert_called_once()

def test_update_employee(service, repository, default_employee):
    repository.update.return_value = default_employee

    result = service.update_employee(default_employee)

    assert result.street_name == "Main Street"
    assert result.work_permit_end is None
    assert result.payment_method == PaymentMethod.BANK_TRANSFER
    assert result.iban == "DE12345678"
    repository.update.assert_called_once_with(default_employee)


def test_list_active_employees(service, repository):
    expiry_date = date(2026, 12, 31)
    repository.get_active_employees.return_value = [
        EmployeeContractInfo(
            last_name="Doe", first_name="John", contract_end=date(2026,12,31)
        ),
        EmployeeContractInfo(
            last_name="Miller", first_name="Glen", contract_end=None
        )
    ]

    result = service.list_active_employees(expiry_date)

    assert len(result) == 2
    assert result[0].last_name == "Doe"
    assert result[0].contract_end == date(2026,12,31)
    assert result[1].contract_end is None
    repository.get_active_employees.assert_called_once_with(expiry_date)
