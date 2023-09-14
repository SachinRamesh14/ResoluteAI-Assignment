import time

from pageObjects.LoginPage import Login
from Utilities import customlogger
from Utilities.readproperties import ReadConfig

class Test_Login:
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.loginobj = Login(self.driver)

        self.logger.info("****** Nagative Login test ******")
        self.loginobj.EnterEmail("abc123@gmail.com")
        self.loginobj.EnterPassword("face123")
        self.loginobj.ClickLogin()

        self.loginobj.Cleardata()

        self.logger.info("****** Positive Login test ******")
        self.loginobj.EnterEmail(self.email)
        self.loginobj.EnterPassword(self.password)
        self.loginobj.ClickLogin()

        self.validatelogin = self.loginobj.Validatelogin()

        if self.validatelogin == True:
            self.logger.info("******** Login successfully testcase passed ***********")
            assert True

        else:
            self.logger.info("********* Testcase Falied ***********")
            self.driver.close()
            assert False


        self.logger.info("****** Log Out Test ******")
        time.sleep(15)
        self.loginobj.ClickLogOut()
        self.loginobj.ClickOk()

        self.validatelogout = self.loginobj.Validatelogout()

        if self.validatelogout == True:
            self.logger.info("****** logout successfully tasecase passed ******")
            self.driver.close()
            assert True

        else:
            self.logger.info("****** Testcase Failed ******")
            self.driver.close()
            assert False

        self.logger.info("******* test_01_login IS COMPLETED **********")