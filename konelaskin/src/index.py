import sys
from entities.calculation import Calculation

def main():
    calculation = Calculation()
    string = input("Anna laskutoimitus: ")
    print(calculation.calculate(string))
    return

if __name__== "__main__":
    main()