import allure
import pytest
from Web.Pages.signUp_page import SignUp_Page
from Web.Utils.utils import Utils
from Web.Base.base_test import Base_Page


class Test_SignUp(Base_Page):

    @allure.description('Successfully Display SignUp page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_SignUp_page_from_Header_SignUp_options(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()

    @allure.description('SignUp using valid username and password which popup alert message')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_valid_username_and_password(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("Samson22")
        signUp.enter_Password("12345")
        signUp.click_SignUp_Button()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('SignUp using Invalid username and password which popup alert message "Please fill out Username and Password." ')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_not_providing_username_and_password(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.click_SignUp_Button()
        signUp.Assert_alert_fill_error()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('SignUp using Invalid username and Valid password which popup alert message "Please fill out Username and Password." ')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_Invalid_username_and_Valid_password(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("")
        signUp.enter_Password("12345")
        signUp.click_SignUp_Button()
        signUp.Assert_alert_fill_error()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('SignUp using valid username and Invalid password which popup alert message "Please fill out Username and Password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_Valid_username_and_Invalid_password(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("David")
        signUp.enter_Password("")
        signUp.click_SignUp_Button()
        signUp.Assert_alert_fill_error()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('SignUp using Special Character on userName which popup alert message "Please fill out Username and Password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_SpecialCharacter_on_userName(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("@!@!@!")
        signUp.enter_Password("12345")
        signUp.click_SignUp_Button()  # _____
        signUp.Assert_alert_exist_text1()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('SignUp using Special Character on Password which popup alert message "This user already exist."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_SpecialCharacter_on_Password(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("david")
        signUp.enter_Password("#$%^")
        signUp.click_SignUp_Button()
        signUp.Assert_alert_exist_text1()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('SignUp using Special Character on UserName and Password which popup alert message "This user already exist.."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_SpecialCharacter_on_Username_and_password(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("!@#$")
        signUp.enter_Password("#$%^")
        signUp.click_SignUp_Button()
        signUp.Assert_alert_exist_text1()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('Successfully Close SignUp page Using Closed Button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_SignUp_page_Using_Close_Button(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.click_Close_Button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('Successfully Close SignUp page Using X Button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_SignUp_page_Using_X_Button(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.click_X_Button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('SignUp using valid username and blank password which popup alert message "Please fill out Username and Password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_Valid_username_and_Blank_password(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("David")
        signUp.enter_Password("")
        signUp.click_SignUp_Button()
        signUp.Assert_alert_fill_error()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)

    @allure.description('SignUp using Numbers on username and password which popup alert message "Please fill out Username and Password."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_an_Account_by_providing_Numbers_on_username_and_password(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.click_SignUp_option()
        signUp.enter_UserName("012345")
        signUp.enter_Password("012345")
        signUp.click_SignUp_Button()
        signUp.Assert_alert_exist_text1()
        signUp.click_OK_alert_button()
        Utils(driver).assertion(signUp.title, self.driver.title)
