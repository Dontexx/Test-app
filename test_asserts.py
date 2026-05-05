# test_asserts.py
from converter_logic import convert_currency

def test_convert_correct():
    result = convert_currency(1000, "USD", rates={"USD": 27.5})
    assert result == 1000 / 27.5, f"Expected {1000/27.5}, got {result}"

def test_convert_unknown_currency():
    try:
        convert_currency(100, "XXX", rates={"USD": 27.5})
        assert False, "Should raise KeyError"
    except KeyError:
        pass  # Очікуваний виняток

def test_convert_negative_amount():
    result = convert_currency(-500, "USD", rates={"USD": 27.5})
    assert result < 0, "Negative amount should remain negative"

if __name__ == "__main__":
    test_convert_correct()
    test_convert_unknown_currency()
    test_convert_negative_amount()
    print("All assert tests passed!")