### Hexlet tests and linter status:
[![Actions Status](https://github.com/Sozercaya/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Sozercaya/python-project-49/actions)
# Brain Games

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Sozercaya_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Sozercaya_python-project-49)

[![asciicast](https://asciinema.org/a/782DYvR55sKF5Viu.svg)](https://asciinema.org/a/782DYvR55sKF5Viu)

## Описание

**Brain Games** — это набор консольных игр для тренировки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы.

### Доступные игры:
- **brain-games** — приветствие и знакомство с игроком
- **brain-even** — проверка числа на четность (нужно ответить "yes" или "no")
- *Другие игры в разработке*

## Установка

### Требования
- Python 3.15 или выше
- uv (рекомендуется) или pip

### Установка через uv
```bash
# Клонируйте репозиторий
git clone git@github.com:Sozercaya/python-project-49.git
cd python-project-49

# Соберите и установите пакет
make build
make package-install

Использование
После установки запустите игру командой:

bash
# Приветствие
brain-games

# Игра "Четное/нечетное"
brain-even
Пример работы
https://asciinema.org/a/782DYvR55sKF5Viu.svg

# Игра "Калькулятор"
brain-calc
Пример работы
https://asciinema.org/a/LygLu8ue18E0X4Rd

# Игра "НОД"
brain-gcd
Пример работы
https://asciinema.org/a/x2TPIEKsGjVzNnIt

# Игра "Арифметическая прогрессия"
brain-progression
Пример работы
https://asciinema.org/a/pIizvxxKcoKPEikT

# Игра "Простое ли число?"
brain-prime
Пример работы
https://asciinema.org/a/JU2o3BH5TjqUZmyr


Разработка
Настройка окружения
bash
# Создайте виртуальное окружение
uv venv

# Активируйте
source .venv/bin/activate

# Установите зависимости
uv sync
Запуск локально (без установки)
bash
uv run python -m brain_games.scripts.brain_games
uv run python -m brain_games.scripts.brain_even
Линтинг
bash
uv run ruff check brain_games
Автор
Sozercaya