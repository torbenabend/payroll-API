from datetime import date, timedelta


def get_month_range(month: int, year: int) -> tuple[date, date]:
    start = date(year, month, 1)
    if month == 12:
        end = date(year + 1, 1, 1)
    else:
        end = date(year, month + 1, 1)
    return start, end


def get_business_days_in_month(month: int, year: int) -> int:
    _, start_next_month = get_month_range(month, year)
    last_day = start_next_month - timedelta(days=1)
    business_days = 0
    for day in range(1, last_day.day + 1):
        if date(year, month, day).weekday() < 5:
            business_days += 1
    return business_days
