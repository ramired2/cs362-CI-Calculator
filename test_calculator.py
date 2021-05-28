"""
test for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert  5 == calculator.add(3, 2)

    def test_subtract(self):
        assert  1 == calculator.subtract(3, 2)

    def test_multiply(self):
        assert  6 == calculator.multiply(3, 2)

    def test_divide(self):
        assert  2 == calculator.divide(4, 2)