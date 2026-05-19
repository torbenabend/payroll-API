from __future__ import annotations

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class UserDB(Base):
    __tablename__ = "users"

    # Primary key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # User information
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)

    # Foreign keys
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False
    )
    employee_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("employees.id"),
        nullable=True
    )

    # Relationships
    role: Mapped["RoleDB"] = relationship(back_populates="users")

    def __str__(self):
        return self.username
