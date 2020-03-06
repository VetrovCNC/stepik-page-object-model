# stepik-page-object-model

## Финальное задание по созданию тестового проекта в рамках обучения на курсе: Автоматизация тестирования с помощью Selenium и Python ( https://stepik.org/course/575 )

### Инструкция по запуску

Создаем новое виртуальное окружение и активируем его

1. `$ python3 -m venv selenium-env --without-pip`
2. `$ . ./.venv/bin/activate`
3. `(selenium-env)$ curl https://bootstrap.pypa.io/get-pip.py | python3`

Устанавливаем зависимости:

4. `(selenium-env)$ pip install -r requirements.txt`

Запускаем скрипт для проверки работы:

5. `(selenium-env)$ pytest -v --tb=line --language=en test_main_page.py`
