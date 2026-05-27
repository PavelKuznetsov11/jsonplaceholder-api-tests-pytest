# JSONPlaceholder API Tests

Проект содержит автоматизированные API-тесты для проверки базовых операций REST API на эндпоинте `/posts` публичного сервиса [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

Тесты написаны на Python с использованием `pytest` и библиотеки `requests`.

## Что проверяется

В проекте проверяются основные операции с ресурсом `/posts`:

- получение списка постов;
- получение поста по `id`;
- обработка запроса к несуществующему посту;
- создание нового поста;
- обновление существующего поста;
- удаление поста.

## Особенность JSONPlaceholder

JSONPlaceholder — это тестовый fake REST API.

Он имитирует операции `POST`, `PUT` и `DELETE`, но не сохраняет изменения на сервере. Поэтому в тестах на создание, обновление и удаление проверяется ответ API: статус-код и данные в теле ответа.

## Структура проекта

```text
jsonplaceholder-api-tests-pytest/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_posts.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Назначение файлов

- `tests/__init__.py` — пустой файл, обозначает директорию `tests` как Python-пакет.
- `tests/conftest.py` — содержит общие фикстуры для тестов:
  - `base_url` — базовый URL API;
  - `api_session` — HTTP-сессия `requests.Session()`.
- `tests/test_posts.py` — содержит тесты для эндпоинта `/posts`.
- `requirements.txt` — список зависимостей проекта.
- `.gitignore` — список файлов и папок, которые не нужно добавлять в Git.
- `README.md` — описание проекта и инструкция по запуску.

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/PavelKuznetsov11/jsonplaceholder-api-tests-pytest.git
```

Перейти в папку проекта:

```bash
cd jsonplaceholder-api-tests-pytest
```

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать виртуальное окружение на Windows:

```bash
venv\Scripts\activate
```

Для macOS/Linux:

```bash
source venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Запустить все тесты:

```bash
pytest tests/ -v
```

## Пример ожидаемого вывода

```text
tests/test_posts.py::TestPosts::test_get_posts_list PASSED
tests/test_posts.py::TestPosts::test_get_post_by_id[1] PASSED
tests/test_posts.py::TestPosts::test_get_post_by_id[2] PASSED
tests/test_posts.py::TestPosts::test_get_post_by_id[3] PASSED
tests/test_posts.py::TestPosts::test_get_not_found_post PASSED
tests/test_posts.py::TestPosts::test_create_post PASSED
tests/test_posts.py::TestPosts::test_update_post PASSED
tests/test_posts.py::TestPosts::test_delete_post PASSED

============================== 8 passed in 1.20s ==============================
```

## Используемые технологии

- Python
- pytest
- requests
- JSONPlaceholder API

## Комментарий по тестам

Тесты не зависят друг от друга и могут запускаться повторно в любом порядке.  
Для HTTP-запросов используется общая сессия `requests.Session()`, которая создаётся через фикстуру `api_session` и закрывается после завершения тестового запуска.
