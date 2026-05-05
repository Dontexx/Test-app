# test_unittest.py
import unittest
from converter_logic import convert_currency, add_to_history, get_history

class TestConverter(unittest.TestCase):
    
    def setUp(self):
        # Перед кожним тестом очищаємо історію
        self.rates = {"USD": 27.5, "EUR": 33.0, "PLN": 6.8}
    
    def test_convert_usd(self):
        result = convert_currency(1000, "USD", self.rates)
        expected = 1000 * 27.5
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_convert_eur(self):
        result = convert_currency(500, "EUR", self.rates)
        expected = 500 / 33.0
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_invalid_currency(self):
        with self.assertRaises(KeyError):
            convert_currency(100, "INVALID", self.rates)
    
    def test_history_append(self):
        add_to_history("100 UAH -> 3.64 USD")
        add_to_history("200 UAH -> 6.06 EUR")
        history = get_history()
        self.assertEqual(len(history), 2)

if __name__ == "__main__":
    unittest.main()