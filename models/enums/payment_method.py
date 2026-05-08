from enum import Enum

class PaymentMethod(str, Enum):
    CASH = "Bar"
    BANK_TRANSFER = "Überweisung"