import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10
    browser.config.window_width = 1200
    browser.config.window_height = 1000

    yield

    browser.quit()

