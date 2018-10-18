import pytest
from unittest import mock
from unittest import TestCase
import mock
from Calculator import Calculator

#test class
class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

    def test_subtraction(self):
        answer = self.calc.subtract(10,5)
        self.assertEqual(answer,5)
    
    def test_division(self):
        answer = self.calc.devide(10,5)
        self.assertEqual(answer,2)
    
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.devide(10,0)

         
    

