# converter_logic.py

def convert_currency(amount: float, currency: str, rates: dict) -> float:
    """Перевіряє конвертацію UAH -> foreign (ділення на курс)"""
    if currency not in rates:
        raise KeyError(f"Невідома валюта: {currency}")
    return amount / rates[currency]

_history = []

def add_to_history(record: str) -> None:
    _history.append(record)

def get_history() -> list:
    return _history.copy()

def clear_history() -> None:
    _history.clear()