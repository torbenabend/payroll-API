from __future__ import annotations

from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class Role(Base):
    __tablename__ =  "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_name: Mapped[str] = mapped_column(String)
    read_employee_data: Mapped[bool] = mapped_column(Boolean)
    edit_employee_data: Mapped[bool] = mapped_column(Boolean)
    process_payroll: Mapped[bool] = mapped_column(Boolean)

    users: Mapped[list["User"]] = relationship(back_populates="role")

    def __str__(self):
        return self.role_name
