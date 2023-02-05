import allure
import pytest
from Web.Pages.login_page import Login_Page
from Web.Utils.utils import Utils
from Web.Base.base_test import Base_Page
from Web.Pages.signUp_page import SignUp_Page
from Web.Pages.logOut_page import LogOut_page


class Test_Login(Base_Page):

    @allure.description('Successfully Display Login page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Login_page_from_Header_Login_options(self):
        driver = self.driver
        signUp = Login_Page(driver)
        signUp.open_Main_page()
        signUp.click_Login_option()

    @allure.description('Login using valid username and password Successfully display login page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Login_an_Account_by_providing_valid_username_and_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("dawit")
        login.enter_Password("12345")
        login.click_Login_Button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description(
        'Login using Invalid username and password which popup alert message "Please fill out Username and Password." ')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Login_an_Account_by_not_providing_username_and_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.click_Login_Button()
        login.Assert_alert_fill_error()
        login.click_OK_alert_button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description('Login using Invalid username and Valid password which popup alert message "Wrong password." ')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Login_an_Account_by_providing_Invalid_username_and_Valid_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("dddddd")
        login.enter_Password("12345")
        login.click_Login_Button()
        login.Assert_alert_wrong_password()
        login.click_OK_alert_button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description(
        'Login using valid username and Invalid password which popup alert message "Please fill out Username and Password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Login_an_Account_by_providing_Valid_username_and_Invalid_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("David")
        login.enter_Password("0000000")
        login.click_Login_Button()
        login.Assert_alert_wrong_password()
        login.click_OK_alert_button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description('Login using Special Character on userName which popup alert message "Wrong password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Login_an_Account_by_providing_SpecialCharacter_on_userName(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("@!@!@!")
        login.enter_Password("12345")
        login.click_Login_Button()
        login.Assert_alert_wrong_password()
        login.click_OK_alert_button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description('Login using Special Character on Password which popup alert message "Wrong password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Login_an_Account_by_providing_SpecialCharacter_on_Password(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.click_Login_option()
        Login.enter_UserName("david")
        Login.enter_Password("#$%^")
        Login.click_Login_Button()
        Login.Assert_alert_wrong_password()
        Login.click_OK_alert_button()
        Utils(driver).assertion(Login.title, self.driver.title)

    @allure.description(
        'Login using Special Character on UserName and Password which popup alert message "Wrong password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_SpecialCharacter_on_Username_and_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("!@#$")
        login.enter_Password("#$%^")
        login.click_Login_Button()
        login.Assert_alert_wrong_password()
        login.click_OK_alert_button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description('Successfully Close Login page Using Closed Button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_SignUp_page_Using_Close_Button(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.click_Close_Button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description('Successfully Close Login page Using X Button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_SignUp_page_Using_X_Button(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.click_X_Button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description(
        'Login using valid username and blank password which popup alert message "Please fill out Username and Password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Login_an_Account_by_providing_Valid_username_and_Blank_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("David")
        login.enter_Password("")
        login.click_Login_Button()
        login.Assert_alert_fill_error()
        login.click_OK_alert_button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description('Login using Numbers on username and password which popup alert message "Wrong password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Login_an_Account_by_providing_Numbers_on_username_and_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("01234567")
        login.enter_Password("01234567")
        login.click_Login_Button()
        login.Assert_alert_User_Not_exist()
        login.click_OK_alert_button()
        Utils(driver).assertion(login.title, self.driver.title)

    @allure.description('Login Successfully Validate Login to account from user SignUp to User logout')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_E2E_Validate_Login_to_account_from_user_SignUp_to_User_logout(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("Dododo")
        signUp.enter_Password("12345")
        signUp.click_SignUp_Button()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("Dododo")
        login.enter_Password("12345")
        login.click_Login_Button()
        Utils(driver).assertion(login.title, self.driver.title)
        logout = LogOut_page(driver)
        logout.click_LogOut_option()
        Utils(driver).assertion(logout.title, self.driver.title)
