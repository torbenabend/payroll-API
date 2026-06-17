from enum import Enum

class Permission(Enum):
    EDIT_EMPLOYEE_DATA = "edit_employee_data"
    READ_EMPLOYEE_DATA = "read_employee_data"
    PROCESS_PAYROLL = "process_payroll"
