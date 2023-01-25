from selenium.webdriver.common.by import By


class AccountRegistrationPage:
    txtbox_firstname_id = "input-firstname"
    txtbox_lastname_id = "input-lastname"
    txtbox_email_id = "input-email"
    txtbox_password_id = "input-password"
    chk_policy_name = "agree"
    btn_continue_xpath = '//button[@type="submit"]'
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def set_firstname(self, name):
        self.driver.find_element(By.ID, self.txtbox_firstname_id).send_keys(name)

    def set_lastname(self, name):
        self.driver.find_element(By.ID, self.txtbox_lastname_id).send_keys(name)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.txtbox_password_id).send_keys(password)

    def click_policy(self):
        self.driver.find_element(By.NAME, self.chk_policy_name).click()

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def get_confirmation_msg(self):
        try:
            return  self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            None