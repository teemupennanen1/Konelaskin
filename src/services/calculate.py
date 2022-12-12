'''Module for calculations'''

numbers = ["0","1","2","3","4","5","6","7","8","9"]
operators = ["+", "-", "*", "/", "!"]

class Calculate:
    '''This is the Class that handles the calculations'''
    def __init__(self):
        self.result = ""
        self.operator = ""
        self.parts = []
        self.actor = ""
        self.negative = False

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
        for constant in calculation:
            if constant == "-" and self.actor == "":
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
                    self.result = self.calculate(self.parts, self.operator)
                self.actor = ""
                self.parts = []
                self.operator = ""
        return self.result

    def calculate(self, parts, operation):
        '''Main method, where operation is defined'''
        self.parts = parts
        self.operation = operation
        if self.operation == "+":
            return self.addition(parts)
        if self.operation == "-":
            return self.subtraction(parts)
        if self.operation == "*":
            return self.multiplication(parts)
        if self.operation == "/":
            return self.division(parts)

    def addition(self, parts):
        '''Method for addition'''
        return 1.0*parts[0] + parts[1]

    def subtraction(self, parts):
        '''Method for subraction'''
        return 1.0*parts[0] - parts[1]

    def multiplication(self, parts):
        '''Method for multiplication'''
        return 1.0*parts[0]*parts[1]

    def division(self, parts):
        '''Method for division'''
        return 1.0* parts[0] / parts[1]
