from collections import Counter
from typing import List, Dict
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(reports: List[Dict]):
        simple_report = SimpleReport.generate(reports)

        companies_counter = Counter(
            [key["nome_da_empresa"] for key in reports]
        )
        companies_and_qtd = ""
        for company_name, quantity in companies_counter.items():
            companies_and_qtd += f"- {company_name}: {quantity}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{companies_and_qtd}"
        )
