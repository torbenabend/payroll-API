from sqlalchemy import Boolean, Column, Float, Integer, String, Date, ForeignKey
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String)
    first_name = Column(String)
    birth_date = Column(Date)
    street_name = Column(String)
    house_number = Column(String)
    postal_code = Column(String) # or Integer?
    city = Column(String)
    IBAN = Column(String)
    tax_class = Column(Integer)
    child_allowance = Column(Float)
    denomination = Column(String)
    contract_start = Column(Date)
    contract_end = Column(Date)
    last_contract_start = Column(Date)
    last_contract_end = Column(Date)
    work_permit_type = Column(String) # limited or unlimited
    work_permit_end = Column(Date)
    permanent_residence_permit = Column(Boolean)
    residence_permit_end = Column(Date)
    social_security_number = Column(String)
    tax_id = Column(String)
    payment_method = Column(String) # cash or bank transfer
    salary_type = Column(String) # fixed or hourly
    salary = Column(Float)
    is_active = Column(Boolean)
    created_by = Column(Integer, ForeignKey("users.id"))

    def __str__(self):
        return f"{self.last_name}, {self.first_name} (Employee-ID: {self.id})"


class WorkLog(Base):
    __tablename__ = "worklogs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date = Column(Date)
    hours_early_shift = Column(Float)
    hours_late_shift = Column(Float)
    hours_night_shift = Column(Float)
    mission_related_allowance = Column(Float)
    weekday = Column(String)
    day_type = Column(String) # normal, public_holiday, sick or vacation
    created_by = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    role = Column(Integer, ForeignKey("roles.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))

    def __str__(self):
        return self.username


class Role(Base):
    __tablename__ =  "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String)
    read_employee_data = Column(Boolean)
    edit_employee_data = Column(Boolean)
    process_payroll = Column(Boolean)

    def __str__(self):
        return self.role_name



