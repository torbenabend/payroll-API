from __future__ import annotations

from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class RoleDB(Base):
    __tablename__ =  "roles"

    # Primary key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Role information
    role_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    read_employee_data: Mapped[bool] = mapped_column(Boolean, nullable=False)
    edit_employee_data: Mapped[bool] = mapped_column(Boolean, nullable=False)
    process_payroll: Mapped[bool] = mapped_column(Boolean, nullable=False)

    # Relationships
    users: Mapped[list["UserDB"]] = relationship(back_populates="role")

    def __str__(self):
        return self.role_name
