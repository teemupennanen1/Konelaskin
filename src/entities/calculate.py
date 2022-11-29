'''Module for calculations'''
class Calculate:
    """This is the Class that handles the calculations"""

    def addition(self, parts):
        '''Method for addition'''
        return parts[0] + parts[1]

    def subtraction(self, parts):
        '''Method for subraction'''
        return parts[0] - parts[1]

    def multiplication(self, parts):
        '''Method for multiplication'''
        if (1.0*parts[0]*parts[1]) % 1 == 0:
            return parts[0]*parts[1]
        return 1.0*parts[0]*parts[1]

    def division(self, parts):
        '''Method for division'''
        if 1.0*parts[0]/parts[1] % 1 == 0:
            return parts[0]//parts[1]
        return 1.0* parts[0] / parts[1]
