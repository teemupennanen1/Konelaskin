"""Main file for running the program"""
from entities.calculation import Calculation
import pygame
"""Importing the module for handling calculations"""
def main():
    """Main loop"""
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    operations = ["+", "-", "*", "/"]
    parts = []
    actor = ""
    operator = ""
    while True:
        new_calculation = Calculation()
        calculator_input = input("")
        if calculator_input in numbers:
            actor += calculator_input
        if calculator_input in operations and actor != "":
            parts.append(int(actor))
            operator = calculator_input
        if calculator_input == "":
            break
        if calculator_input == "=" or pygame.key.get_pressed() == pygame.K_KP_ENTER:
            if len(parts) >= 1:
                print(new_calculation.calculate(parts, operator))
        else:
            print("Error")
        

if __name__== "__main__":
    main()
