# Parser Cny

Парсер юаня для api

## Запуск проекта (без Docker)

### Требования
- Python 3.10+
- Poetry

### Установка без Docker
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kotafan1rich/parser_cny.git
   cd my-awesome-project

2. Установите зависимости:
    ```bash
    poetry install
3. Запустите:
    ```bash
    python3 src/main.py

### Установка с Docker
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kotafan1rich/parser_cny.git
   cd my-awesome-project

2. Запустите:
    ```bash
    docker build -t parser_cny .
    docker run --env-file .env parser_cny
