import pygame
from entities.calculate import Calculate

'''Global variables'''
numbers = ["0","1","2","3","4","5","6","7","8","9"]
operators = ["+", "-", "*", "/"]
addition = "+"
subtraction = "-"
multiplication = "*"
division = "/"

class Konelaskin:
    '''class for the calculator'''
    def __init__(self):
        '''class constructor'''
        self.calculate = Calculate()
        self.calculation = ""
        self.parts = []
        self.operation = ""
        self.right_brackets = 0
        self.left_brackets = 0
        self.actor = ""
        self.result = ""

    def handle_events(self):
        while True:
            self.calculation = input("Anna lauseke:")
            for c in self.calculation:
                if self.calculation == "":
                    break
                if c == "(":
                    self.left_brackets += 1
                if c == ")":
                    self.right_brackets += 1
                if c in numbers:
                    self.actor += c
                if c in operators:
                    self.parts.append(int(self.actor))
                    self.actor = ""
                    self.operation = c
                if c == "=":
                    self.parts.append(int(self.actor))
                    self.actor = ""
                    if self.operation == "+":
                        self.result = self.calculate.addition(self.parts)
                    if self.operation == "-":
                        self.result = self.calculate.subtraction(self.parts)
                    if self.operation == "*":
                        self.result = self.calculate.multiplication(self.parts)
                    if self.operation == "/":
                        self.result = self.calculate.division(self.parts)
                    
            if self.left_brackets == self.right_brackets:
                print(self.result)
                self.result = ""
                
