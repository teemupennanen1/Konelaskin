import unittest
import os
from src.entities.calculate import Calculation

class TestCalculation(unittest.TestCase):
    def setUp(self):
        calculation = Calculation()

    def test_addtition_operator_returns_correct_value(self):
        self.assertEqual(self.calculation.calculate("2+2", 4))
