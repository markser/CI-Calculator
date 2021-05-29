"""
tests for calc app in circle ci
"""
import calculator


class TestCalculatorApp:

    def test_add(self):
        assert 5 == calculator.add(3, 2)
        assert 10000 != calculator.add(3, 2)

    def test_subtract(self):
        assert 1 == calculator.sub(3, 2)
        assert 10000 != calculator.sub(3, 2)

    def test_multiply(self):
        assert 2 == calculator.mul(1, 2)
        assert 10000 != calculator.mul(3, 2)

    def test_divide(self):
        assert 1 == calculator.div(5, 5)
        assert 10000 != calculator.div(3, 2)
