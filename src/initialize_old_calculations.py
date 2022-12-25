import os
from repositories.calculation_repository import CalculationRepository

dirname = os.path.dirname(__file__)

dirname = dirname.replace("src", "data")
filename = "calculations.csv"

fp = os.path.join(dirname, filename)

with open(fp, 'w') as datafile:
    datafile.write("date & time, calculation")
