"""
tests for calc app in circle ci
"""
import calculator


class TestCalculatorApp:

    def test_add(self):
        assert 5 == calculator.add(3,2)


    def test_subtract(self):
        assert 1 == calculator.sub(3,2)
