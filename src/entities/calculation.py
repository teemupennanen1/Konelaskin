class Calculation:
    """This is the Class that handles the calculations"""
    def calculate(self, calculation):
        """This is the method that calculates the calculations"""
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        operations = ["+", "-", "*", "/"]
        parts = []
        calc = ""
        operator = ""
        for c in calculation: # pylint: disable=invalid-name
            if c in numbers:
                calc += c
            else:
                parts.append(int(calc))
                operator = c
                calc = ""
        parts.append(int(calc))
        if operator not in operations:
            return "Error"
        if operator == "+":
            return parts[0] + parts[1]