'''Test module for the program'''
import unittest
from entities.calculate import Calculate

class TestCalculation(unittest.TestCase):
    '''This class is for testing the programs'''
    def setUp(self) -> None:
        self.calculate = Calculate()
        self.parts = [2,2]

    def test_addtition_operator_returns_correct_value(self):
        '''Test for addition operation'''
        self.assertEqual(self.calculate.calculate(self.parts, "+"), 4.0)

    def test_subraction_operator_returns_correct_value(self):
        '''Test for subtraction operation'''
        self.assertEqual(self.calculate.calculate(self.parts, "-"), 0.0)

    def test_multiplication_operator_returns_correct_value_when_natural_number(self):
        '''Test for multiplication operation'''
        self.assertEqual(self.calculate.calculate(self.parts, "*"), 4.0)

    def test_division_operator_returns_correct_value_when_natural_number(self):
        '''Test for division operation'''
        self.assertEqual(self.calculate.calculate(self.parts, "/"), 1.0)
