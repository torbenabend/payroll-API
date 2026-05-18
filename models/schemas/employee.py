from datetime import date, datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, BeforeValidator

from models.enums.payment_method import PaymentMethod
from models.validators.common import parse_date, parse_datetime


class Employee(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None

    last_name: str
    first_name: str
    birth_date: Annotated[date, BeforeValidator(parse_date)]
    tax_id: str | None = None
    social_security_number: str | None = None

    street_name: str
    house_number: str
    postal_code: str
    city: str

    tax_class: int | None = None
    child_allowance: float | None = None
    denomination: str | None = None

    work_permit_end: Annotated[date | None, BeforeValidator(parse_date)] = None
    residence_permit_end: Annotated[date | None, BeforeValidator(parse_date)] = None

    payment_method: PaymentMethod
    iban: str | None = None

    updated_by: int
    updated_at: Annotated[datetime, BeforeValidator(parse_datetime)]
