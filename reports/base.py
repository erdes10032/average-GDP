import csv
from abc import ABC, abstractmethod
from tabulate import tabulate


class BaseReport(ABC):
    """Базовый класс для всех отчетов."""

    def __init__(self, files):
        self.files = files
        self.data = self._read_files()

    def _read_files(self):
        """Читает данные из всех переданных файлов."""
        all_data = []
        for file_path in self.files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        row['gdp'] = float(row['gdp']) if row['gdp'] else 0.0
                        row['year'] = int(row['year'])
                        all_data.append(row)
            except FileNotFoundError:
                raise FileNotFoundError(f"Файл '{file_path}' не найден")
            except KeyError as e:
                raise ValueError(f"В файле '{file_path}' отсутствует обязательная колонка: {e}")

        if not all_data:
            raise ValueError("Не удалось прочитать данные из файлов")

        return all_data

    @abstractmethod
    def generate(self):
        """Генерирует и выводит отчет."""
        pass

    def _display_table(self, headers, rows):
        """Отображает данные в виде таблицы."""
        print(tabulate(rows, headers=headers, tablefmt='grid'))