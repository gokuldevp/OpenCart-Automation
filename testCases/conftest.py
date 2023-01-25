import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.utilities import get_current_date_time
import datetime
import os


# *************************************************** Browser setup ************************************************** #
@pytest.fixture()
def setup(browser):
    """fixture function for Launching the Browser"""
    log_path = None
    if browser == 'edge':
        # log_path = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('testCases\\conftest.py', '')),
        #                         'logs', "edgedriver.log")
        serv_obj = EdgeService(EdgeChromiumDriverManager().install(), log_path=log_path)
        driver = webdriver.Edge(service=serv_obj)
        print("Launching Edge Browser.................")
    elif browser == 'firefox':
        # log_path = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('testCases\\conftest.py', '')),
        # 'logs', "geckodriver.log")
        serv_obj = FirefoxService(GeckoDriverManager().install(), log_path=log_path)
        driver = webdriver.Firefox(service=serv_obj)
        print("Launching Firefox Browser..............")
    else:
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('testCases\\conftest.py', '')),
                                'logs', "chromedriver.log")
        serv_obj = ChromeService(ChromeDriverManager().install(), log_path=log_path)
        driver = webdriver.Chrome(service=serv_obj)
        print("Launching Chrome Browser...............")
    return driver


def pytest_addoption(parser):
    """Function to get the value from Command line"""
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    """function to return the browser value to the setup method"""
    return request.config.getoption("--browser")


# ********************************************** Pytest HTML Report ************************************************** #
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Hook for adding Environment info to HTML report"""
    session.config._metadata["Project Name"] = "Opencart"
    session.config._metadata["Module Name"] = "Login Module"
    session.config._metadata["Tester Name"] = "Gokul Dev P"
    session.config._metadata["OS Name"] = "Windows 11"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    """Hook for Deleting/Modify Environment info to HTML report"""
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Generating reports and saving them in report folder"""
    timestamp = datetime.datetime.strptime(get_current_date_time(), '%Y%m%d%H%M%S').strftime('%d_%m_%Y %H-%M-%S')
    config.option.htmlpath = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('testCases\\', '')), 'reports', f'report_{timestamp}.html')
