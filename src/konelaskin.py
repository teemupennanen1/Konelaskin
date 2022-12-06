'''Calculator module'''
from entities.calculate import Calculate

numbers = ["0","1","2","3","4","5","6","7","8","9"]
operators = ["+", "-", "*", "/"]

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
        self.shutdown = "e"

    def shutdown_handler(self):
        while True:
            command = input("Suljetaanko? K/e: ")
            if command == "K" or command == "k":
                self.shutdown = "K"
                return
            if command == "E" or command == "e":
                self.shutdown = "E"
                return
            else:
                print("Sopimaton komento")

    def calculation_handler(self):
        for constant in self.calculation:
            if constant == "(":
                self.left_brackets += 1
            if constant == ")":
                self.right_brackets += 1
            if constant in numbers or constant == ".":
                self.actor += constant
            if constant in operators:
                self.parts.append(int(self.actor))
                self.actor = ""
                self.operation = constant
            if constant == "=":
                self.parts.append(int(self.actor))
                self.result = self.calculate.calculate(self.parts, self.operation)
                self.actor = ""
                self.parts = []

    def handle_events(self):
        '''Function for handling the calculator inputs'''
        while True:
            self.calculation = input("Anna lauseke: ")
            if self.calculation == "":
                self.shutdown_handler()
                if self.shutdown == "K":
                    break
            if self.calculation != "":
                if self.calculation[-1] != "=":
                    print("Muista = merkki viimeiseksi")
                else:
                    self.calculation_handler()
            if self.left_brackets == self.right_brackets:
                if self.shutdown == "K":
                    break
                if self.result != "":
                    print(self.result)
                self.result = ""
