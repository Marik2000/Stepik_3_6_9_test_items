import pytest, time
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose your language: ")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    page_language = request.config.getoption("language")
    link = "http://selenium1py.pythonanywhere.com/" + page_language + "/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    yield browser
    print("\nquit browser..")
    browser.quit()
