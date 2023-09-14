from selenium.webdriver.common.by import By

class AddLicense:

    txt_managelicense_xpath = "//span[contains(text(),'Manage Licenses')]"
    button_addlicense_xpath = "//p[contains(text(),'Add License')]"
    txtbox_employeeid_xpath = "//input[@name='empId']"
    txtbox_firstname_xpath = "//input[@name='firstName']"
    txtbox_lastname_xpath = "//input[@name='lastName']"
    txtbox_phoneNo_xpath = "//input[@name='phoneNumber']"
    txtbox_busNo_xpath = "//input[@name='busNo']"
    txtbox_email_xpath = "//input[@name='email']"
    txtbox_password_xpath = "//input[@name='password']"
    button_submit_xpath = "//p[contains(text(),'Submit Details')]"

    def __init__(self, driver):
        self.driver = driver

    def GoToLicensepage(self):
        self.driver.find_element(By.XPATH, self.txt_managelicense_xpath).click()

    def ClickAddLicense(self):
        self.driver.find_element(By.XPATH,  self.button_addlicense_xpath).click()

    def Firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtbox_firstname_xpath).send_keys(firstname)

    def Lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txtbox_lastname_xpath).send_keys(lastname)

    def Phonenumber(self, phoneNo):
        self.driver.find_element(By.XPATH, self.txtbox_phoneNo_xpath).send_keys(phoneNo)

    def BusNo(self, busNo):
        self.driver.find_element(By.XPATH, self.txtbox_busNo_xpath).send_keys(busNo)

    def Email(self, email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

    def Password(self, password):
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).send_keys(password)

    def Submit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

