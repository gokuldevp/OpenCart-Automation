from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from pageObjects.my_account_page import MyAccountPage
from utilities.utilities import ScreenShots as SS, ReadConfig as RC, LogGen, Excel, TestData


class Test003LoginDDT:
    url = RC.get_application_url()
    logger = LogGen.loggen()
    testdata_file = TestData.get_login_test_data()

    def test_valid_login(self, setup):
        self.logger.info("**** Test 003 login data driven testing ****")
        self.row = Excel.get_row_count(self.testdata_file, "Sheet1")
        self.lst_status = []

        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.map = MyAccountPage(self.driver)

        for r in range(2, self.row+1):
            self.hp.click_myaccount()
            SS.take_screenshots_as_png(self.driver, f"Test 003 {r} navigating to login page ")
            self.logger.info("**** Navigating to Login page ****")
            self.hp.click_login()

            self.email = Excel.read_data(self.testdata_file, "Sheet1", r, 1)
            self.password = Excel.read_data(self.testdata_file, "Sheet1", r, 2)
            self.expected = Excel.read_data(self.testdata_file, "Sheet1", r, 3)
            self.logger.info(f"**** Getting the Email:{self.email} and Password:{self.password} ****")

            self.logger.info("**** Entering user information ****")
            self.lp.set_email(self.email)
            self.lp.set_password(self.password)

            SS.take_screenshots_as_png(self.driver, f"Test 003 {r} enter_user_information")
            self.lp.click_login()
            self.logger.info("**** submit user information ****")
            self.target_page = self.lp.is_my_account_page_exists()
            SS.take_screenshots_as_png(self.driver, f"Test 003 {r} result")
            if self.expected == "Valid":
                if self.target_page:
                    self.lst_status.append("PASS")
                    Excel.write_data(self.testdata_file, "Sheet1", r, 4, "PASS")
                    Excel.fill_green_color(self.testdata_file, "Sheet1", r, 4)
                    self.map.click_logout()
                else:
                    Excel.write_data(self.testdata_file, "Sheet1", r, 4, "FAIL")
                    Excel.fill_red_color(self.testdata_file, "Sheet1", r, 4)
                    self.lst_status.append("FAIL")
            elif self.expected == "Invalid":
                if self.target_page:
                    Excel.write_data(self.testdata_file, "Sheet1", r, 4, "FAIL")
                    Excel.fill_red_color(self.testdata_file, "Sheet1", r, 4)
                    self.lst_status.append("FAIL")
                    self.map.click_logout()
                else:
                    Excel.write_data(self.testdata_file, "Sheet1", r, 4, "PASS")
                    Excel.fill_green_color(self.testdata_file, "Sheet1", r, 4)
                    self.lst_status.append("PASS")
        self.driver.close()

        if "FAIL" in self.lst_status:
            self.logger.error("**** Test Failed ****")
            assert False
        else:
            self.logger.info("**** Test Passed ****")
            assert True




