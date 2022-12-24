import os
from repositories.calculation_repository import CalculationRepository

dirname = os.path.dirname("./data")

old_calculations_repository = CalculationRepository(os.path.join(dirname, "..", "data",
"calculations.csv"))