from datetime import date

from pydantic import BaseModel, field_serializer


class EmployeeContractInfo(BaseModel):
    first_name: str
    last_name: str
    contract_end: date | None

    @field_serializer("contract_end")
    def serialize_contract_end(self, value):
        return "unbefristet" if value is None else value
