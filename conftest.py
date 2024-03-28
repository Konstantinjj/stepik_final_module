import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FOptions


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Specify the language for the browser (e.g., 'en', 'fr', etc.)")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")

    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        # Инициализируем Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        # Инициализируем Firefox
        options = FOptions()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
