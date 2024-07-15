from abc import ABC, abstractmethod
import json
import csv

class Exporter(ABC):
    @abstractmethod
    def export(self, data, file_path):
        pass

class JsonExporter(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

class CsvExporter(Exporter):
    def export(self, data, file_path):
        if data:
            keys = data[0].keys()
            with open(file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
