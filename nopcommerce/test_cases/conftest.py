import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome',
                     help='Specify the browser: chrome or firefox or edge')


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported error")
    return driver


# For pytest html reports
# hook for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, nopcommerce'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'KHAJAVALI'


# hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA HOME', None)
    metadata.pop('Plugins', None)
