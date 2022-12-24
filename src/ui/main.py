'''Calculator module'''
from services.calculate import Calculate
from repositories.calculation_repository import CalculationRepository

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

    def options_handler(self):
        '''Function for displaying the different options available for the program'''
        print("Voit laskea laskutoimituksia kirjoittamalla ne Anna lauseke: merkkijonon perään \n"
        "ja painamalla Enter-näppäintä. Muista lisätä laskutoimituksen perään =-merkki! \n"
        "Kirjoittamalla ohjeet ja painamalla Enter-näppäintä ohjelma tulostaa tämän näkymän \n"
        "Tyhjä rivi ja Enter-näppäin käynnistää laskimen sammutustoiminnon \n"
        "Vastaamalla K tai k, laskin sammutetaan \n"
        "Vastaamalla E tai e jatketaan laskimen käyttöä")

    def print_result(self):
        '''Function for printing the result of the calculation. This function ensures
        that the result is a number'''
        if self.result != None:
            print(self.result)

    def handle_events(self):
        '''Function for handling the calculator inputs'''
        while True:
            self.calculation = input("Anna laskutoimitus: ")
            if self.calculation.casefold() == "ohjeet":
                self.options_handler()
                continue
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
                self.print_result()
                self.result = ""
