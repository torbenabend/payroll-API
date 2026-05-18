from datetime import date, datetime

def parse_date(value: str) -> date | None:
    if isinstance(value, date) or value is None:
        return value
    return datetime.strptime(value,"%d/%m/%Y").date()


def parse_datetime(value: str) -> datetime:
    if isinstance(value, datetime):
        return value
    return datetime.strptime(value,"%d/%m/%Y")
