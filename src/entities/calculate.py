class Calculate:
    """This is the Class that handles the calculations"""
    result = None

    def __ini__(self):
        self.calculate = Calculate()
        self.result = ""

    def calculate(self, parts, operation):
        """This is the method that calculates the calculations"""
        if operation == "+":
            self.addition(parts)

    def addition(self, parts):
        return(parts[0] + parts[1])

    def subtraction(self, parts):
        return(parts[0] - parts[1])

    def multiplication(self, parts):
        return(1.0* parts[0] * parts[1])

    def division(self, parts):
        return(1.0* parts[0] / parts[1])
