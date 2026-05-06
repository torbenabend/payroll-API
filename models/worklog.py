from __future__ import annotations
from datetime import date, datetime

from sqlalchemy import Float, Integer, String, Date,DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class WorkLog(Base):
    __tablename__ = "worklogs"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("employees.id")
    )
    date: Mapped[date] = mapped_column(Date)
    hours_early_shift: Mapped[float] = mapped_column(Float)
    hours_late_shift: Mapped[float] = mapped_column(Float)
    hours_night_shift: Mapped[float] = mapped_column(Float)
    mission_related_allowance: Mapped[float] = mapped_column(Float)
    weekday: Mapped[str] = mapped_column(String)
    day_type: Mapped[str] = mapped_column(String) # normal, public_holiday, sick or vacation
    updated_by: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    employee: Mapped["Employee"] = relationship(back_populates="worklogs")
    user: Mapped["User"] = relationship(back_populates="worklog_entries")
