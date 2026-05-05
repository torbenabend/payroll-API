from __future__ import annotations
from datetime import date, datetime
from typing import Optional

from sqlalchemy import Float, Integer, String, Date,DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base
from models import Contract, WorkLog


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    last_name: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    birth_date: Mapped[date] = mapped_column(Date)
    street_name: Mapped[str] = mapped_column(String)
    house_number: Mapped[str] = mapped_column(String)
    postal_code: Mapped[str] = mapped_column(String)
    city: Mapped[str] = mapped_column(String)
    IBAN: Mapped[str] = mapped_column(String)
    tax_class: Mapped[int] = mapped_column(Integer)
    child_allowance: Mapped[float] = mapped_column(Float)
    denomination: Mapped[str] = mapped_column(String)
    work_permit_end: Mapped[Optional[date]] = mapped_column(
        Date, nullable=True
    )
    residence_permit_end: Mapped[Optional[date]] = mapped_column(
        Date, nullable=True
    )
    social_security_number: Mapped[str] = mapped_column(String)
    tax_id: Mapped[str] = mapped_column(String)
    payment_method: Mapped[str] = mapped_column(String) # cash or bank transfer
    updated_by: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    contracts: Mapped[list["Contract"]] = relationship(
        back_populates="employee"
    )
    worklogs: Mapped[list["WorkLog"]] = relationship(back_populates="employee")

    def __str__(self):
        return f"{self.last_name}, {self.first_name} (Employee-ID: {self.id})"
