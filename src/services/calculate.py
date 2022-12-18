'''Module for calculations'''

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
operators = ["+", "-", "*", "/", "!", "="]
answer = "ans"

class Calculate:
    '''This is the Class that handles the calculations'''
    def __init__(self):
        self.result = ""
        self.operator = ""
        self.parts = []
        self.actor = ""
        self.negative = False
        self.answer = ""

    def check_operator(self, constant):
        if self.operator == "+" and constant == "+":
            self.operator = "+"
            return
        if self.operator == "-" and constant == "+":
            self.operator = "-"
            return
        if self.operator == "-" and constant == "-":
            self.operator = "+"
            return
        if self.operator == "+" and constant == "-":
            self.operator = "-"
            return
    
    def append_actor(self):
        if self.negative:
            self.parts.append(-1.0*float(self.actor))
            self.negative = False
            return
        self.parts.append(float(self.actor))

    def calculation_logic(self, calculation):
        '''Function for breaking appart the calculation string'''
        while "ans" in calculation.casefold() and self.answer != "":
            calculation = calculation.casefold().replace("ans", str(self.answer))
        for constant in calculation:
            if constant not in numbers and constant not in operators:
                print("Epävalidi kaava")
                return
            if constant == "-" and len(self.parts) == 0 and self.actor == "":
                self.negative = True
                continue
            if constant in numbers or constant == ".":
                self.actor += constant
            if constant in operators:
                if self.operator == "":
                    self.append_actor()
                    self.actor = ""
                    self.operator = constant
                else:
                    self.check_operator(constant)
            if constant == "=":
                self.append_actor()
                if len(self.parts) == 2:
                    self.result = self.calculate()
                self.actor = ""
                self.parts = []
                self.operator = ""
        self.answer = self.result
        return self.result

    def calculate(self):
        '''Main method, where operation is defined'''
        if self.operator == "+":
            return self.addition()
        if self.operator == "-":
            return self.subtraction()
        if self.operator == "*":
            return self.multiplication()
        if self.operator == "/":
            return self.division()

    def addition(self):
        '''Method for addition'''
        return 1.0*self.parts[0] + self.parts[1]

    def subtraction(self):
        '''Method for subraction'''
        return 1.0*self.parts[0] - self.parts[1]

    def multiplication(self):
        '''Method for multiplication'''
        return 1.0*self.parts[0]*self.parts[1]

    def division(self):
        '''Method for division'''
        return 1.0* self.parts[0] / self.parts[1]
