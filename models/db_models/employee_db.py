from __future__ import annotations
from datetime import date, datetime

from sqlalchemy import (Float, Integer, String, Date,DateTime, ForeignKey,
                        Enum as SQLEnum)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base
from models.enums.payment_method import PaymentMethod


class EmployeeDB(Base):
    __tablename__ = "employees"

    # Primary key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Personal data
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)
    tax_id: Mapped[str | None] = mapped_column(String, nullable=True, unique=True)
    social_security_number: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
        unique=True
    )

    # Address
    street_name: Mapped[str] = mapped_column(String, nullable=False)
    house_number: Mapped[str] = mapped_column(String, nullable=False)
    postal_code: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String, nullable=False)

    # Payroll data
    tax_class: Mapped[int | None] = mapped_column(Integer, nullable=True)
    child_allowance: Mapped[float | None] = mapped_column(Float, nullable=True)
    denomination: Mapped[str | None] = mapped_column(String, nullable=True)

    # Legal information
    work_permit_end: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )
    residence_permit_end: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    # Payment information
    payment_method: Mapped[PaymentMethod] = mapped_column(
        SQLEnum(PaymentMethod),
        nullable=False
    )
    iban: Mapped[str | None] = mapped_column(String, nullable=True)

    # Audit fields
    updated_by: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # Relationships
    contracts: Mapped[list["ContractDB"]] = relationship(
        back_populates="employee"
    )
    worklogs: Mapped[list["WorkLogDB"]] = relationship(back_populates="employee")

    def __str__(self):
        return f"{self.last_name}, {self.first_name} (Employee-ID: {self.id})"
