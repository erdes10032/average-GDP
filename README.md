# Макроэкономический анализатор данных

Скрипт для обработки CSV файлов с макроэкономическими данными и генерации отчетов.

## Установка

**1. Клонируйте репозиторий**

```bash
git clone https://github.com/erdes10032/average-GDP.git
cd average-GDP
```

**2. Создать виртуальное окружение**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

**3. Установите зависимости**

```bash
pip install -r requirements.txt
```

**4. Запустите программу**

```bash
python main.py --files examples/economic1.csv examples/economic2.csv --report average-gdp
```

## Тесты

**Все тесты**
```bash
python -m pytest tests/
```

**С покрытием кода**

```bash
python -m pytest tests/ --cov=reports --cov=main
```

**Подробный вывод**

```bash
python -m pytest tests/ -v
```