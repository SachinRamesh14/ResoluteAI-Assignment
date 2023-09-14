from selenium.webdriver.common.by import By

class Login:

    txtbox_email_xpath = "//input[@id='email']"
    txtbox_password_xpath = "//input[@id='password']"
    button_login_xpath = "//button[@type='submit']"
    txt_mailid_xpath = "//*[contains(text(),'testbams@gmail.com')]"
    button_logout_xpath = "//span[contains(text(),'Log Out')]"
    button_Ok_xpath = "//*[contains(text(),'Ok')]"

    def __init__(self, driver):
        self.driver = driver

    def EnterEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

    def EnterPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def Cleardata(self):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).clear()

    def Validatelogin(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_mailid_xpath).is_displayed()
        except:
            return False

    def ClickLogOut(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def ClickOk(self):
        self.driver.find_element(By.XPATH, self.button_Ok_xpath).click()

    def Validatelogout(self):
        try:
            return self.driver.find_element(By.XPATH, self.button_login_xpath).is_displayed()
        except:
            return False