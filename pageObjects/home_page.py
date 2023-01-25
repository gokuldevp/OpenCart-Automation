from selenium.webdriver.common.by import By


class HomePage:
    lnk_myaccount_linktxt = "My Account"
    lnk_register_linktxt = "Register"
    lnk_login_linktxt = "Login"

    def __init__(self, driver):
        self.driver = driver

    def click_myaccount(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_myaccount_linktxt).click()

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_register_linktxt).click()

    def click_login(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktxt).click()
