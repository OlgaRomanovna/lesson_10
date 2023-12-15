import pytest
from selene.support import shared as _shared


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser = _shared.browser
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10
    browser.config.window_width = 1200
    browser.config.window_height = 1000

    yield

    browser.quit()
