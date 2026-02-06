from .base import BaseReport


class AverageGdpReport(BaseReport):
    """Отчет со средним ВВП по странам."""

    def generate(self):
        country_data = {}

        for row in self.data:
            country = row['country']
            gdp = row['gdp']

            if country not in country_data:
                country_data[country] = {
                    'total_gdp': 0.0,
                    'count': 0
                }

            country_data[country]['total_gdp'] += gdp
            country_data[country]['count'] += 1

        results = []
        for country, data in country_data.items():
            avg_gdp = data['total_gdp'] / data['count']
            results.append({
                'country': country,
                'avg_gdp': avg_gdp
            })

        results.sort(key=lambda x: x['avg_gdp'], reverse=True)
        headers = ["", "country", "gdp"]
        rows = []

        for i, result in enumerate(results, 1):
            rows.append([
                i,
                result['country'],
                f"{result['avg_gdp']:.2f}"
            ])

        self._display_table(headers, rows)
        return results