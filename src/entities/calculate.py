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
        result = 0
        for p in parts:
            result += p
        return str(result)