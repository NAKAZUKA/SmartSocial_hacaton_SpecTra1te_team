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

## Использование и эксплуатация

### Локальное использование

1. Поднимите сервис на DRF:
    - Запустите сервер из директории `museum_admin_drf-main`:
        ```sh
        cd museum_admin_drf-main
        source venv/bin/activate  # Для Windows: venv\Scripts\activate
        python manage.py runserver
        ```

2. Запустите Telegram бота в другом терминале:
    - Из директории `bot_museum-main`:
        ```sh
        cd bot_museum-main
        source venv/bin/activate  # Для Windows: venv\Scripts\activate
        python main.py
        ```

3. Поднимите сервис аудиогида с GPS системой на сервере или локально:
    - Из директории `WOLK-speaker`:
        ```sh
        cd WOLK-speaker
        source venv/bin/activate  # Для Windows: venv\Scripts\activate
        python main.py
        ```

### Деплой

Для продакшен использования вы можете осуществить деплой всех сервисов:
- Сервис на DRF и Telegram бот могут быть размещены на сервере (например, через Docker или любой другой хостинг).
- Сервис аудиогида с GPS системой может быть размещен на отдельном сервере для обработки запросов от пользователей.

На данный момент реализация предусмотрена для локального взаимодействия. Дополнительные шаги по деплою и настройке могут потребовать настройки веб-сервера (например, Nginx), системы управления процессами (например, Supervisor) и других инструментов.
