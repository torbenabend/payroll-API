from __future__ import annotations
from datetime import date

from sqlalchemy import (Float, Integer, String, Date, ForeignKey,
                        Enum as SQLEnum)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base
from models.enums.day_type import DayType


class WorkLogDB(Base):
    __tablename__ = "worklogs"

    # Primary key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Shift data
    date: Mapped[date] = mapped_column(Date, nullable=False)
    hours_early_shift: Mapped[float] = mapped_column(Float, nullable=True)
    hours_late_shift: Mapped[float] = mapped_column(Float, nullable=True)
    hours_night_shift: Mapped[float] = mapped_column(Float, nullable=True)
    weekday: Mapped[str] = mapped_column(String, nullable=False)
    day_type: Mapped[DayType | None] = mapped_column(
        SQLEnum(DayType),
        nullable=True
    )
    mission_related_allowance: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    # Foreign key
    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("employees.id")
    )

    # Relationships
    employee: Mapped["EmployeeDB"] = relationship(back_populates="worklogs")
