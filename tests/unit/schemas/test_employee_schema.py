import pytest
from datetime import date

from pydantic import ValidationError

from models import Employee
from models.enums.payment_method import PaymentMethod


@pytest.fixture
def valid_test_data() -> dict:
    return {
        "last_name": "Doe",
        "first_name": "John",
        "birth_date": "02/09/1980",
        "street_name": "Main Street",
        "house_number": "45a",
        "postal_code": "1234",
        "city": "Springfield",
        "payment_method": PaymentMethod.BANK_TRANSFER
    }


class FakeEmployee:
    def __init__(self):
        self.id = 4
        self.last_name = "Doe"
        self.first_name = "John"
        self.birth_date = "02/09/1980"
        self.street_name = "Main Street"
        self.house_number = "45a"
        self.postal_code = "1234"
        self.city = "Springfield"
        self.payment_method = PaymentMethod.BANK_TRANSFER


def test_employee_creation_assigns_fields_and_default_values(valid_test_data):
    employee = Employee(**valid_test_data)

    assert employee.last_name == "Doe"
    assert employee.first_name == "John"
    assert employee.birth_date.year == 1980
    assert employee.payment_method == PaymentMethod.BANK_TRANSFER
    assert employee.social_security_number is None
    assert employee.work_permit_end is None


def test_employee_missing_fields():
    data = {"last_name": "01/01/2024"}
    with pytest.raises(ValidationError):
        Employee(**data)


def test_employee_wrong_type(valid_test_data):
    valid_test_data["tax_id"] = 1234
    with pytest.raises(ValidationError):
        Employee(**valid_test_data)


def test_employee_parse_dates(valid_test_data):
    valid_test_data["work_permit_end"] = "31/12/2026"
    valid_test_data["residence_permit_end"] = "31/12/2026"
    employee = Employee(**valid_test_data)

    assert isinstance(employee.work_permit_end, date)
    assert isinstance(employee.residence_permit_end, date)


def test_employee_invalid_date(valid_test_data):
    valid_test_data["work_permit_end"] = "not-a-date"
    with pytest.raises(ValidationError):
        Employee(**valid_test_data)


def test_employee_enum_payment_method(valid_test_data):
    valid_test_data["payment_method"] = "not-a-valid-payment-method"
    with pytest.raises(ValidationError):
        Employee(**valid_test_data)


def test_employee_from_attributes():
    fake_employee = FakeEmployee()
    employee = Employee.model_validate(fake_employee)

    assert employee.id == 4
    assert employee.last_name == "Doe"
    assert employee.first_name == "John"
    assert employee.birth_date.year == 1980
    assert employee.street_name == "Main Street"
    assert employee.house_number == "45a"
    assert employee.postal_code == "1234"
    assert employee.city == "Springfield"
    assert employee.payment_method == PaymentMethod.BANK_TRANSFER
    assert employee.social_security_number is None
    assert employee.work_permit_end is None
