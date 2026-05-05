from __future__ import annotations
from datetime import date, datetime

from sqlalchemy import Float, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base
from models import Employee


class Contract(Base):
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("employees.id")
    )
    contract_start: Mapped[date] = mapped_column(Date)
    contract_end: Mapped[date] = mapped_column(Date)
    salary_type: Mapped[str] = mapped_column(String)
    fixed_salary: Mapped[float] = mapped_column(Float)
    hourly_rate: Mapped[float] = mapped_column(Float)
    updated_by: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    employee: Mapped["Employee"] = relationship(back_populates="contracts")
