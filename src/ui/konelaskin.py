'''Calculator module'''
from services.calculate import Calculate

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
        self.actor = ""
        self.result = ""
        self.shutdown = "e"

    def shutdown_handler(self):
        '''Function for handling the shutdown of the program'''
        while True:
            command = input("Suljetaanko? K/e: ")
            if command in ("K", "k"):
                self.shutdown = "K"
                return
            if command in ("E", "e"):
                self.shutdown = "E"
                return
            print("Sopimaton komento")

    def handle_events(self):
        '''Function for handling the calculator inputs'''
        while True:
            self.calculation = input("Anna lauseke: ")
            if self.calculation == "":
                self.shutdown_handler()
                if self.shutdown == "K":
                    break
                self.calculation = ""
            if len(self.calculation) != 0:
                if self.calculation[-1] != "=":
                    print("Muista = merkki viimeiseksi")
                else:
                    self.result = self.calculate.calculation_logic(self.calculation)
            if self.result != "":
                if self.shutdown == "K":
                    break
                print(self.result)
                self.result = ""
