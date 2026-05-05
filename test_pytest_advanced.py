import pytest
from converter_logic import convert_currency, add_to_history, get_history, clear_history

# Фікстура для підготовки курсів та чистої історії
@pytest.fixture
def rates():
    return {"USD": 27.5, "EUR": 33.0, "PLN": 6.8}

@pytest.fixture
def clean_history():
    clear_history()
    yield
    clear_history()  # очищення після тесту

# Параметризований тест конвертації
@pytest.mark.parametrize("amount, currency, expected", [
    (100, "USD", 100 / 27.5),
    (200, "EUR", 200 / 33.0),
    (300, "PLN", 300 / 6.8),
    (0, "USD", 0)
])
def test_conversion(amount, currency, expected, rates):
    result = convert_currency(amount, currency, rates)
    assert round(result, 2) == round(expected, 2)

# Другий тест з параметризацією для невалідних валют
@pytest.mark.parametrize("invalid_currency", ["XXX", "usd", "EuR", ""])
def test_invalid_currency(invalid_currency, rates):
    with pytest.raises(KeyError):
        convert_currency(100, invalid_currency, rates)

# Тест, який очікує помилку
def test_convert_with_string_raises():
    with pytest.raises(TypeError):
        convert_currency("сто", "USD", {"USD": 27.5})

@pytest.mark.skip(reason="Функція округлення ще не реалізована")
def test_rounding():
    result = convert_currency(100, "USD", {"USD": 27.5})
    assert result == 3.64

@pytest.mark.xfail(reason="Відома помилка: негативна сума не обробляється окремо")
def test_negative_amount():
    result = convert_currency(-50, "USD", {"USD": 27.5})
    assert result >= 0, "Конвертер не повинен повертати від'ємні значення"

def test_fail_intentionally():
    assert convert_currency(10, "USD", {"USD": 27.5}) == 1000

def test_fail_due_to_exception():
    convert_currency(10, None, {"USD": 27.5})