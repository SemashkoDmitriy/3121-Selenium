import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Укажите какой язык будете использовать: ru, es, fr, de и т.д.")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Укажите какой ,браузер будете использовать: chrome или firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    browser = None
    if browser_name == "chrome":
        print("\nЗапускаем браузер Chrome для тестирования..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        print("\nЗапускаем браузер Firefox для тестирования..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name Должен быть chrome or firefox")
    yield browser
    print("\nЗакрываем браузер..")
    browser.quit()