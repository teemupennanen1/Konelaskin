import os
from repositories.calculation_repository import CalculationRepository

dirname = os.path.dirname(__file__)

wordlist_repository = CalculationRepository(os.path.join(dirname, "..", "data",
"calculations.csv"))