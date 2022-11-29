import pygame
from entities.calculation import Calculation

'''Global variables'''
numbers = ["0","1","2","3","4","5","6","7","8","9"]
basic_operations = ["+", "-", "*", "/"]

class Konelaskin:
    '''class for the calculator'''
    def __init__(self):
        '''class constructor'''

    def handle_events(self):
        actors = []
        actor = ""
        operator = ""
        while True:
            new_calculation = Calculation()
            calculator_input = input("")
            if calculator_input in numbers:
                actor += calculator_input
            if calculator_input in basic_operations and actor != "":
                actors.append(int(actor))
                operator = calculator_input
            if calculator_input == "":
                break
            if calculator_input == "=":
                if actor != "":
                    actors.append(int(actor))
                if len(actors) >= 2:
                    print(new_calculation.calculate(actors, operator))
                    actors = []
                    operator = ""
                    actor = ""
            else:
                print("Error")
