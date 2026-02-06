import pytest
import tempfile
import sys
import os
from reports.average_gdp import AverageGdpReport

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

class TestAverageGdpReport:
    """Тесты для отчета среднего ВВП."""

    def create_test_csv(self, content):
        """Создает временный CSV файл с заданным содержимым."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(content)
            return f.name

    def test_single_file_single_country(self):
        """Тест с одним файлом и одной страной."""
        csv_content = """country,year,gdp,gdp_growth,inflation,unemployment,population,continent
USA,2023,100.0,2.1,3.4,3.7,339,North America
USA,2022,200.0,2.1,8.0,3.6,338,North America"""

        file_path = self.create_test_csv(csv_content)

        try:
            report = AverageGdpReport([file_path])
            results = report.generate()

            assert len(results) == 1
            assert results[0]['country'] == 'USA'
            assert results[0]['avg_gdp'] == 150.0
        finally:
            os.unlink(file_path)

    def test_multiple_files_multiple_countries(self):
        """Тест с несколькими файлами и странами."""
        csv1_content = """country,year,gdp,gdp_growth,inflation,unemployment,population,continent
USA,2023,100.0,2.1,3.4,3.7,339,North America
China,2023,50.0,5.2,2.5,5.2,1425,Asia"""

        csv2_content = """country,year,gdp,gdp_growth,inflation,unemployment,population,continent
USA,2022,200.0,2.1,8.0,3.6,338,North America
China,2022,100.0,3.0,2.0,5.6,1423,Asia"""

        file1 = self.create_test_csv(csv1_content)
        file2 = self.create_test_csv(csv2_content)

        try:
            report = AverageGdpReport([file1, file2])
            results = report.generate()
            assert len(results) == 2
            assert results[0]['country'] == 'USA'
            assert results[0]['avg_gdp'] == 150.0
            assert results[1]['country'] == 'China'
            assert results[1]['avg_gdp'] == 75.0
        finally:
            os.unlink(file1)
            os.unlink(file2)

    def test_empty_file(self):
        """Тест с пустым файлом."""
        csv_content = "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"

        file_path = self.create_test_csv(csv_content)

        try:
            with pytest.raises(ValueError, match="Не удалось прочитать данные из файлов"):
                report = AverageGdpReport([file_path])
                report.generate()
        finally:
            os.unlink(file_path)

    def test_file_not_found(self):
        """Тест с несуществующим файлом."""
        with pytest.raises(FileNotFoundError):
            report = AverageGdpReport(['nonexistent.csv'])
            report.generate()

    def test_missing_gdp_column(self):
        """Тест с файлом без колонки GDP."""
        csv_content = """country,year,gdp_growth,inflation,unemployment,population,continent
USA,2023,2.1,3.4,3.7,339,North America"""

        file_path = self.create_test_csv(csv_content)

        try:
            with pytest.raises(ValueError, match="отсутствует обязательная колонка"):
                report = AverageGdpReport([file_path])
                report.generate()
        finally:
            os.unlink(file_path)