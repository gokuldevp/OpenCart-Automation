from selenium.webdriver.common.by import By


class LoginPage:
    txt_email_id = "input-email"
    txt_password_id = "input-password"
    btn_login_xpath = "//button[text()='Login']"
    msg_myaccount_xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def is_my_account_page_exists(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
        except Exception:
            return False
