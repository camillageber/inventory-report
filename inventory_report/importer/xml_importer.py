import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if (path.endswith('.xml')):
            with open(path) as file:
                report = xmltodict.parse(file.read())['dataset']['record']
            return report
        else:
            raise ValueError('Arquivo inválido')
