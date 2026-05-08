from __future__ import annotations
from datetime import date, datetime

from sqlalchemy import Float, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class Contract(Base):
    __tablename__ = "contracts"

    # Primary key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Contract data
    contract_start: Mapped[date] = mapped_column(Date, nullable=False)
    contract_end: Mapped[date | None] = mapped_column(Date, nullable=True)
    salary_type: Mapped[str] = mapped_column(String, nullable=False)
    fixed_salary: Mapped[float | None] = mapped_column(Float, nullable=True)
    hourly_rate: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Audit fields
    updated_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # Foreign keys
    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("employees.id"), nullable=False
    )

    # Relationships
    employee: Mapped["Employee"] = relationship(back_populates="contracts")
