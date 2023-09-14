import time
from pageObjects.LicensePage import AddLicense
from pageObjects.LoginPage import Login
from Utilities import customlogger
from Utilities.readproperties import ReadConfig

class Test_Student:
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()


    def testcase_addstudent(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)

        self.loginobj = Login(self.driver)
        self.logger.info("****** Login ******")
        self.loginobj.EnterEmail(self.email)
        self.loginobj.EnterPassword(self.password)
        self.loginobj.ClickLogin()
        time.sleep(15)

        self.licenseobj = AddLicense(self.driver)
        self.licenseobj.GoToLicensepage()
        self.licenseobj.ClickAddLicense()
        self.licenseobj.Firstname("itachi")
        self.licenseobj.Lastname("uchiha")
        self.licenseobj.Phonenumber("7709843210")
        self.licenseobj.BusNo("19c")
        self.licenseobj.Email("abc123@gmail.com")
        self.licenseobj.Password("Xyz@1000")
        self.licenseobj.Submit()

        self.logger.info("****** Add License successfully ******")
        self.driver.close()
        self.logger.info("****** test_03_license completed ******")

