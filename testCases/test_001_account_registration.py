from pageObjects.home_page import HomePage
from pageObjects.account_registration_page import AccountRegistrationPage
from utilities.utilities import CreateUser as CU, ScreenShots as SS, ReadConfig as RC, LogGen


class TestAccountRegistration:
    logger = LogGen.loggen()
    url = RC.get_application_url()

    def test_account_reg(self, setup):
        self.logger.info("**** test 001 AccountRegistration Started ****")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)

        self.hp = HomePage(self.driver)
        self.regpage = AccountRegistrationPage(self.driver)

        self.hp.click_myaccount()
        self.logger.info("**** Navigating to Registration page ****")
        self.hp.click_register()

        self.logger.info("**** Entering user information ****")
        self.regpage.set_firstname("ttpvt")
        self.regpage.set_lastname("Gokul")
        self.email = CU.create_email()
        self.regpage.set_email(self.email)
        self.regpage.set_password("abcdefghijklmnop")
        self.regpage.click_policy()
        SS.take_screenshots_as_png(self.driver, "test_001_account_registration")
        self.regpage.click_continue()
        self.logger.info("**** Submitted user information ****")
        self.confmsg = self.regpage.get_confirmation_msg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("**** test 001 AccountRegistration Passed ****")
            self.driver.close()
            assert True
        else:
            SS.take_screenshots_as_png(self.driver, "test_001_account_registration")
            self.logger.error("**** test 001 AccountRegistration Failed ****")
            self.driver.close()
            assert False
        self.logger.info("**** test 001 AccountRegistration Ended ****")
