Финальное задание к курсу "Автоматизация тестирования с помощью Selenium и Python". https://stepik.org/course/575/syllabus

1) Перейдите в корневую папку проекта и создайте виртуальное окружение с помощью команды python3:
python3 -m venv venv

2) Активируйте окружение:
source venv/bin/activate

3) Перед запуском тестов установите пакеты: 
pip install -r requirements.txt

Если возникает ошибка ImportError: attempted relative import with no known parent package, просто удалите точки перед пакетами в тесте. То есть было "from .pages.basket_page import BasketPage", должно стать "from pages.basket_page import BasketPage".
