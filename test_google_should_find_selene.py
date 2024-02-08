"""
3. Доработайте тест на поиск в google с первого занятия с Pytest

4. Установите размер браузера с помощью фикстуры Pytest

5. Добавьте еще один тест на поиск, который проверит, что поиск не выдает результатов по вашему запросу:

    вводим строку, по которой не ожидаем результатов (придумайте случайный набор символов)
    проверяем, что поиск не выдает результатов, и пишет об этом сообщение
"""

from selene import browser, be, have
import pytest

@pytest.fixture(scope='session')
def browser_settings():
    # настройка размера браузера
    browser.config.window_height = 600
    browser.config.window_width = 800
    yield
    browser.quit()


def test_search_have_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('dakjshdlkjahslkjdhlakjshdlkajhsldkjhaklsjndlkjsndlkcfjasldkjbalksdjvbaksjhv').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))


