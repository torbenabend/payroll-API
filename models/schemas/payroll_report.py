from pydantic import BaseModel, ConfigDict, field_serializer, computed_field

from constants import DEFAULT_HOURS_OVERTIME_CALCULATION, NIGHT_SHIFT_PREMIUM, SUNDAY_PREMIUM, HOLIDAY_PREMIUM

class EmployeeInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str
    last_name: str
    street_name: str
    house_number: str
    postal_code: str
    city: str


class Period(BaseModel):
    month: int
    year: int


class WorkingHours(BaseModel):
    early_shift: float = 0.0
    late_shift: float = 0.0
    night_shift: float = 0.0
    sunday: float = 0.0
    holiday: float = 0.0
    holiday_pay: float = 0.0
    vacation: float = 0.0
    sick: float = 0.0
    overtime: float = 0.0

    @computed_field
    @property
    def total(self) -> float:
        return (
            self.early_shift
            + self.late_shift
            + self.night_shift
            + self.sunday
            + self.holiday
            + self.holiday_pay
            + self.vacation
            + self.sick
        )

    def apply_overtime(self, business_days: int):
        target_hours = business_days * DEFAULT_HOURS_OVERTIME_CALCULATION
        self.overtime = self.total - target_hours


class TaxablePay(BaseModel):
    base: float = 0.0
    holiday: float = 0.0
    vacation: float = 0.0
    sick: float = 0.0
    overtime: float = 0.0
    average_wage: float

    @computed_field
    @property
    def total(self) -> float:
        return (
            self.base
            + self.holiday
            + self.vacation
            + self.sick
            + self.overtime
        )

    def calculate(self, working_hours: WorkingHours, hourly_rate):
        overtime_premium_pay = 0.25
        self.base = working_hours.total * hourly_rate
        self.holiday = working_hours.holiday_pay * self.average_wage
        self.vacation = working_hours.vacation * self.average_wage
        self.sick = working_hours.sick * self.average_wage
        self.overtime = (
                working_hours.overtime
                * hourly_rate
                * overtime_premium_pay)

    @field_serializer(
        "base",
        "holiday",
        "vacation",
        "sick",
        "overtime",
        "average_wage"
    )
    def serialize_money(self, value: float) -> float:
        return round(value, 2)


class PremiumPay(BaseModel):
    wage_night_shift: float = 0.0
    wage_sunday: float = 0.0
    wage_holiday: float = 0.0
    night_shift: float = 0.0
    sunday: float = 0.0
    holiday: float = 0.0

    @computed_field
    @property
    def total(self) -> float:
        return self.night_shift + self.sunday + self.holiday

    def calculate(self, working_hours: WorkingHours, hourly_rate: float):
        self.wage_night_shift = hourly_rate * NIGHT_SHIFT_PREMIUM
        self.wage_sunday = hourly_rate * SUNDAY_PREMIUM
        self.wage_holiday = hourly_rate * HOLIDAY_PREMIUM
        self.night_shift = working_hours.night_shift * self.wage_night_shift
        self.sunday = working_hours.sunday * self.wage_sunday
        self.holiday = working_hours.holiday * self.wage_holiday

    @field_serializer(
        "wage_night_shift",
        "wage_sunday",
        "wage_holiday",
        "night_shift",
        "sunday",
        "holiday"
    )
    def serialize_money(self, value: float) -> float:
        return round(value, 2)


class PayrollReport(BaseModel):
    employee_info: EmployeeInfo
    period: Period
    working_hours: WorkingHours
    taxable_pay: TaxablePay
    premium_pay: PremiumPay
