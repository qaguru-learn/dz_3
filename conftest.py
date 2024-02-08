import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_settings():
    # настройка размера браузера
    browser.config.window_height = 600
    browser.config.window_width = 800

