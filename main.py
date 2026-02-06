import argparse
from reports import ReportFactory
import sys


def main():
    parser = argparse.ArgumentParser(
        description='Генерация отчетов из CSV файлов с макроэкономическими данными'
    )
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Пути к CSV файлам с данными'
    )
    parser.add_argument(
        '--report',
        choices=['average-gdp'],
        required=True,
        help='Тип отчета для генерации'
    )

    args = parser.parse_args()

    try:
        report = ReportFactory.create_report(args.report, args.files)
        report.generate()

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()