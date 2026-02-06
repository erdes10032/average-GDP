from .average_gdp import AverageGdpReport


class ReportFactory:
    """Создание отчетов."""

    _reports = {
        'average-gdp': AverageGdpReport
    }

    @classmethod
    def create_report(cls, report_type, files):
        """Создает отчет указанного типа."""
        if report_type not in cls._reports:
            raise ValueError(f"Неизвестный тип отчета: {report_type}")

        return cls._reports[report_type](files)