import pytest

from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from utilities.utilities import ScreenShots as SS, ReadConfig as RC, LogGen, Excel, TestData


class TestLogin:
    url = RC.get_application_url()
    logger = LogGen.loggen()
    testdata_file = TestData.get_login_test_data()

    @pytest.mark.sanity
    def test_valid_login(self, setup):
        self.logger.info("**** test 002 test valid login ****")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)

        self.hp.click_myaccount()
        SS.take_screenshots_as_png(self.driver, "Test 002 1 home_page")
        self.logger.info("**** Navigating to Login page ****")
        self.hp.click_login()

        self.logger.info("**** Entering user information ****")
        self.email = Excel.read_data(self.testdata_file, "Sheet1", 2, 1)
        self.lp.set_email(self.email)
        self.password = Excel.read_data(self.testdata_file, "Sheet1", 2, 2)
        self.lp.set_password(self.password)
        SS.take_screenshots_as_png(self.driver, "Test 002 2 enter_user_information")
        self.lp.click_login()
        self.logger.info("**** submit user information ****")
        if self.lp.is_my_account_page_exists():
            SS.take_screenshots_as_png(self.driver, "Test 002 3 Test Passed")
            self.logger.info("**** Test 001 test Valid Login tested Passed ****")
            assert True
        else:
            self.logger.error("**** Test 001 test Valid Login tested Fail ****")
            SS.take_screenshots_as_png(self.driver, "Test 002 3 Failed")
            assert False




