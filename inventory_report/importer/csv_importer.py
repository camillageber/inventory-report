import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            report = csv.DictReader(file)
            return [data for data in report]
