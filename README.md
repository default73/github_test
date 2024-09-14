# Test GitHub API

## Требования

Для запуска теста необходимы следующие компоненты:

- Python 3.12
- Установленные зависимости из `requirements.txt`

## Установка

### 1. Клонирование репозитория

Склонируйте репозиторий компьютер:

```bash
git clone https://github.com/default73/github_test.git
cd github_test
```

### 2. Создание и активация виртуального окружения

Для Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Для macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск теста

```bash
python test_api.py
```