# SmartSocial_hacaton_SpecTra1te_team

Этот проект включает три основных компонента:
1. Бот для Telegram (`bot_museum-main`)
2. Сервис управления данными музея с API и админ-панелью (`museum_admin_drf-main`)
3. Сервис аудиогида с GPS системой (`WOLK-speaker`)

## Установка и запуск

### 1. Telegram Бот (`bot_museum-main`)

Этот бот предоставляет пользователям возможность узнавать информацию о музее и перенаправляет их на основной сайт с аудиогидом.

#### Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/NAKAZUKA/SmartSocial_hacaton_SpecTra1te_team.git
    cd bot_museum-main
    ```

2. Создайте виртуальное окружение и установите зависимости:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Запустите бота:
    ```sh
    python main.py
    ```

### 2. Сервис управления данными музея с API и админ-панелью (`museum_admin_drf-main`)

Этот сервис предоставляет API и админ-панель для управления данными музея.

#### Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/NAKAZUKA/SmartSocial_hacaton_SpecTra1te_team.git
    cd museum_admin_drf-main
    ```

2. Создайте виртуальное окружение и установите зависимости:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Выполните миграции и создайте суперпользователя:
    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    ```

4. Запустите сервер:
    ```sh
    python manage.py runserver
    ```

### 3. Сервис аудиогида с GPS системой (`WOLK-speaker`)

Этот сервис предоставляет пользователям аудиогид и использует GPS для определения их местоположения.

#### Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/NAKAZUKA/SmartSocial_hacaton_SpecTra1te_team.git
    cd WOLK-speaker
    ```

2. Создайте виртуальное окружение и установите зависимости:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Запустите сервер:
    ```sh
    python main.py
    ```

## Структура проекта

- `bot_museum-main/`: Исходный код Telegram бота
- `museum_admin_drf-main/`: Сервис управления данными музея с API и админ-панелью
- `WOLK-speaker/`: Сервис аудиогида с GPS системой

