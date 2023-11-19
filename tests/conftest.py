import pytest
from selene.support import shared as _shared  # noqa
from selene.support import shared as _shared
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser = _shared.browser
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
