import time
from selenium.webdriver.common.by import By


class AddStudent:

    txt_studentmenu_xpath = "//span[contains(text(),'Manage Student')]"
    button_addstudent_xpath = "//div[1]/div[1]/button"
    txtbox_admissionNo_xpath = "//input[@name='admissionNo']"
    txtbox_firstname_xpath = "//input[@name='firstName']"
    txtbox_lastname_xpath = "//input[@name='lastName']"
    txtbox_fathername_xpath = "//input[@name='fathersName']"
    dropdown_Class_xpath = "//form/div/div[3]/div[2]/div/div"
    select_class_xpath = "//li[@data-value='CLASS 3']"
    dropdown_divison_xpath = "//form/div/div[3]/div[3]/div"
    select_divison_xpath = "//li[@data-value='A']"
    dropdown_gender_xpath = "//form/div/div[4]/div[1]/div"
    select_genter_xpath = "//li[@data-value='M']"
    txtbox_mblNo_xpath = "//input[@name='mobileNo']"
    dropdown_busNo_xpath = "//form/div/div[4]/div[3]/div/div"
    select_busNo_xpath = "//li[@data-value='BUS NO 45 CG-04E-3200']"
    select_DOB_xpath = "//input[@name='dateOfBirth']"
    dropdown_paysts_xpath = "//form/div/div[5]/div[2]/div/div"
    select_paysts_xpath = "//li[@data-value='Yes']"
    dropdown_register_xpath = "//form/div/div[5]/div[3]/div/div"
    select_register_xpath = "//li[@data-value='Yes']"
    dropdown_Area_xpath = "//form/div/div[6]/div[1]/div/div"
    select_area_xpath = "//li[@tabindex='0']"
    txtbox_address_xpath = "//input[@name='address']"
    select_admissiondate_xpath = "//input[@name='admissionDate']"
    button_submit_xpath = "//div[9]/button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def GotoStudentpage(self):
        self.driver.find_element(By.XPATH, self.txt_studentmenu_xpath).click()

    def ClickAddStudent(self):
        self.driver.find_element(By.XPATH, self.button_addstudent_xpath).click()

    def AdmissionNo(self, admissionNo):
        self.driver.find_element(By.XPATH, self.txtbox_admissionNo_xpath).send_keys(admissionNo)

    def Firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtbox_firstname_xpath).send_keys(firstname)

    def Lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txtbox_lastname_xpath).send_keys(lastname)

    def Fathername(self, fathername):
        self.driver.find_element(By.XPATH, self.txtbox_fathername_xpath).send_keys(fathername)

    def SelectClass(self):
        self.driver.find_element(By.XPATH, self.dropdown_Class_xpath).click()
        self.driver.find_element(By.XPATH, self.select_class_xpath).click()

    def SelectDivison(self):
        self.driver.find_element(By.XPATH, self.dropdown_divison_xpath).click()
        self.driver.find_element(By.XPATH, self.select_divison_xpath).click()

    def SelectGenter(self):
        self.driver.find_element(By.XPATH, self.dropdown_gender_xpath).click()
        self.driver.find_element(By.XPATH, self.select_genter_xpath).click()

    def MobileNo(self, mobileNo):
        self.driver.find_element(By.XPATH, self.txtbox_mblNo_xpath).send_keys(mobileNo)

    def SelectBusNo(self):
        self.driver.find_element(By.XPATH, self.dropdown_busNo_xpath).click()
        self.driver.find_element(By.XPATH, self.select_busNo_xpath).click()

    def DateOfbirth(self, DOB):
        self.driver.find_element(By.XPATH, self.select_DOB_xpath).send_keys(DOB)

    def PaymentStatus(self):
        self.driver.find_element(By.XPATH, self.dropdown_paysts_xpath).click()
        self.driver.find_element(By.XPATH, self.select_paysts_xpath).click()

    def Register(self):
        self.driver.find_element(By.XPATH, self.dropdown_register_xpath).click()
        self.driver.find_element(By.XPATH, self.select_register_xpath).click()

    def Area(self):
        self.driver.find_element(By.XPATH, self.dropdown_Area_xpath).click()
        self.driver.find_element(By.XPATH, self.select_area_xpath).click()

    def Address(self, address):
        self.driver.find_element(By.XPATH, self.txtbox_address_xpath).send_keys(address)

    def AdmissionDate(self, admissiondate):
        self.driver.find_element(By.XPATH, self.select_admissiondate_xpath).send_keys(admissiondate)

    def Submit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

