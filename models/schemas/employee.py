from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from models.enums.payment_method import PaymentMethod


class Employee(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None

    last_name: str
    first_name: str
    birth_date: date
    tax_id: str | None = None
    social_security_number: str | None = None

    street_name: str
    house_number: str
    postal_code: str
    city: str

    tax_class: int | None = None
    child_allowance: int | None = None
    denomination: str | None = None

    work_permit_end: date | None = None
    residence_permit_end: date | None = None

    payment_method: PaymentMethod
    iban: str | None = None

    updated_by: int
    updated_at: datetime
