Финальное задание к курсу "Автоматизация тестирования с помощью Selenium и Python". https://stepik.org/course/575/syllabus

Перед запуском тестов необходимо установить пакеты: pip install -r requirements.txt

Если возникает ошибка ImportError: attempted relative import with no known parent package, просто удалите точки перед пакетами в тесте. То есть было "from .pages.basket_page import BasketPage", должно стать "from pages.basket_page import BasketPage".
