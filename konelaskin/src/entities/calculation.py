class Calculation:

    def calculate(self, calculation):
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        operations = ["+", "-", "*", "/"]
        parts = []
        calc = ""
        operator = ""
        for c in calculation:
            if c in numbers:
                calc += c
            if c in operations:
                parts.append(int(calc))
                operator = c
                calc = ""
        parts.append(int(calc))
        if operator == "+":
            return parts[0] + parts[1]