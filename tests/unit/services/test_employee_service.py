import pytest
from unittest.mock import Mock
from datetime import date

from services.employee_service import EmployeeService
from models import Employee
from models.enums.payment_method import PaymentMethod


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

    result = service.create_employee(
        last_name="Doe", first_name="John", birth_date=date(1980,6,5),
        tax_id="1234", social_security_number="1234",
        street_name="Main Street", house_number="45a", postal_code="5555",
        city="Springfield", tax_class=1, child_allowance=0.0,
        denomination="catholic", work_permit_end=None,
        residence_permit_end=None, payment_method=PaymentMethod.BANK_TRANSFER,
        iban="DE12345678"
    )

    assert result.last_name == "Doe"
    assert result.birth_date.year == 1980
    assert result.work_permit_end is None
    assert result.payment_method == PaymentMethod.BANK_TRANSFER
