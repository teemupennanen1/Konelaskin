'''Test module for the program'''
import unittest
from entities.calculate import Calculate

class TestCalculation(unittest.TestCase):
    '''This class is for testing the programs'''
    def setUp(self) -> None:
        self.calculate = Calculate()
        self.parts = [2,2]

    def test_addtition_operator_returns_correct_value(self):
        '''Test for addition'''
        self.assertEqual(self.calculate.addition(self.parts), 4)

    def test_subraction_operator_returns_correct_value(self):
        '''Test for addition'''
        self.assertEqual(self.calculate.subtraction(self.parts), 0)

    def test_multiplication_operator_returns_correct_value_when_natural_number(self):
        '''Test for addition'''
        self.assertEqual(self.calculate.multiplication(self.parts), 4)

    def test_division_operator_returns_correct_value_when_natural_number(self):
        '''Test for addition'''
        self.assertEqual(self.calculate.division(self.parts), 1)
