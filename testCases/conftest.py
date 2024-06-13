from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="default_value", help="Description of the custom option.")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


"================== Pytest HTML Report ==================="

def pytest_configure(config):
    config._metadata = {
        "Tester": "Amal",
        "Project Name": "Hybrid Framework Practice",
    }


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins" , None)
    metadata.pop("Packages", None)
    metadata.pop("Python", None)
    metadata.pop("Capabilities", None)
    metadata.pop("Platform", None)

