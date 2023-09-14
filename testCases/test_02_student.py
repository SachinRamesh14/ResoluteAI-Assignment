import time
from pageObjects.StudentPage import AddStudent
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

        self.studentobj = AddStudent(self.driver)
        self.studentobj.GotoStudentpage()
        self.studentobj.ClickAddStudent()
        self.studentobj.AdmissionNo("14072000")
        self.studentobj.Firstname("Naruto")
        self.studentobj.Lastname("uzumaki")
        self.studentobj.Fathername("minato")
        self.studentobj.SelectClass()
        time.sleep(3)
        self.studentobj.SelectDivison()
        self.studentobj.SelectGenter()
        self.studentobj.MobileNo("9876543210")
        self.studentobj.SelectBusNo()
        self.studentobj.DateOfbirth("05/07/2010")
        self.studentobj.PaymentStatus()
        self.studentobj.Register()
        self.studentobj.Area()
        self.studentobj.Address("29,east street,chennai")
        self.studentobj.AdmissionNo("12345")
        self.studentobj.Submit()

        self.logger.info("***** bug find *****")
        self.driver.close()
        self.logger.info("***** test_02_student completed *****")

