from datetime import datetime
from typing import List, Dict
from collections import Counter


def converted_date(string: str):
    return datetime.strptime(string, "%Y-%m-%d")


class SimpleReport:
    @staticmethod
    def generate(reports: List[Dict]):
        fabrication_date = [
            converted_date(item["data_de_fabricacao"]) for item in reports
            ]
        oldest_manufacturing_date = min(fabrication_date).strftime('%Y-%m-%d')
        expiration_date = [
            converted_date(item["data_de_validade"]) for item in reports
            ]
        current_date = datetime.now()
        closest_expiration_date = min(
            date for date in expiration_date if date > current_date
            ).strftime('%Y-%m-%d')
        companies = [item["nome_da_empresa"] for item in reports]
        more_occurences_company = Counter(companies).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {more_occurences_company}"
            )
