import os
from pathlib import Path
from repositories.calculation_repository import CalculationRepository

dirname = os.path.dirname(__file__)
print(dirname)

dirname = dirname.replace("src", "data/calculations.csv")
print(dirname)

with open(dirname, 'w') as file:
    file.write("date & time, calculation")
