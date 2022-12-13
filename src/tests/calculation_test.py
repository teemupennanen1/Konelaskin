'''Test module for the calculations'''
import unittest
from services.calculate import Calculate

class TestCalculation(unittest.TestCase):
    '''This class is for testing the programs'''
    def setUp(self) -> None:
        self.calculate = Calculate()

    def test_addtition_operator_returns_correct_value(self):
        '''Test for addition operation'''
        self.assertEqual(self.calculate.calculation_logic("2+2="), 4.0)

    def test_subraction_operator_returns_correct_value(self):
        '''Test for subtraction operation'''
        self.assertEqual(self.calculate.calculation_logic("2-2="), 0.0)

    def test_multiplication_operator_returns_correct_value_when_natural_number(self):
        '''Test for multiplication operation'''
        self.assertEqual(self.calculate.calculation_logic("2*2="), 4.0)

    def test_division_operator_returns_correct_value_when_natural_number(self):
        '''Test for division operation'''
        self.assertEqual(self.calculate.calculation_logic("2/2="), 1.0)

    def test_first_actor_can_be_negative(self):
        '''Test for the case when the first actor is negative'''
        self.assertEqual(self.calculate.calculation_logic("-2+2="), 0.0)

    def test_multiple_plus_operators_return_right_answer(self):
        '''Test for multiple plus operator'''
        self.assertEqual(self.calculate.calculation_logic("2++2="), 4.0)

    def test_multiple_minus_operators_return_right_answer(self):
        '''Test for multiple minus operators'''
        self.assertEqual(self.calculate.calculation_logic("2--2="), 4.0)

    def test_odd_number_of_minus_operators_recognized_as_negative(self):
        '''Test for odd number of minus operators'''
        self.assertEqual(self.calculate.calculation_logic("2-+2="), 0.0)

    def test_even_number_of_minus_operators_recognized_as_negative(self):
        '''Test for even number of minus operators'''
        self.assertEqual(self.calculate.calculation_logic("2--2="), 4.0)

    def test_plus_as_first_operator_is_tested_as_well(self):
        '''Test when first operator is + and second is minus'''
        self.assertEqual(self.calculate.calculation_logic("2+-2="), 0.0)