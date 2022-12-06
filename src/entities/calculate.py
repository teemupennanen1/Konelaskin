'''Module for calculations'''
class Calculate:
    '''This is the Class that handles the calculations'''
    def __init__(self):
        self.result = ""
        self.operation = ""
        self.parts = ""

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
