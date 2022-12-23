from datetime import datetime
from pathlib import Path

class CalculationRepository:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.old_calculations = self.find_all()
        self.write(self.old_calculations)

    def ensure_file_exists(self):
        Path(self.file_path).touch()

    def find_all(self):
        '''Return all the saved old calculations'''
        return self.read()

    def read(self):
        old_calculations = []

        self.ensure_file_exists()

        with open(self.file_path, encoding="UTF-8") as file:
            row_count = 0
            for row in file:
                if row_count == 0:
                    row_count = 1
                    continue
                row = row.replace("\n", "")
                parts = row.split(",")
                old_calculations.append((parts[0], parts[1]))
            return old_calculations

    def write(self, old_calculations):

        self.ensure_file_exists()

        with open(self.file_path, "w", encoding="UTF-8") as file:
            file.write("date,time,calculation\n")
            for calculation in old_calculations:
                file.write(f"{calculation[0]}, {calculation[1]}\n")

    def append_calculations(self, calculation):
        date_and_time = datetime.now()
        date_and_time = str(date_and_time)[:19]
        print(self.old_calculations)
        self.old_calculations.append(date_and_time, calculation)
        self.write(self.old_calculations)
