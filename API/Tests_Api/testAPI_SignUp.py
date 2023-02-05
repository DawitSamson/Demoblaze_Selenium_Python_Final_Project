from API.locators_Api.login_locators import Login_Locators
import allure
import pytest
from API.Pages_Api.SignUp_page import SignUp_Page


class Test_Login(SignUp_Page):
    @allure.description('SignUp correctly using Valid UserName and Password')
    @pytest.mark.sanity
    def test_SignUp_correctly(self):
        url = Login_Locators.url_login
        data = Login_Locators.valid_UserName_and_password
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 200)
        SignUp.Assert_Elapsed_time(url, data, 5)  # less than the given second

    @allure.description('SignUp when password incorrectly')
    def test_SignUp_with_incorrectly_password(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_password
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 400)
        SignUp.Assert_Elapsed_time(url, data, 5)

    @allure.description('SignUp when UserName incorrectly')
    def test_SignUp_with_incorrectly_UserName(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_UserName
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 400)
        SignUp.Assert_Elapsed_time(url, data, 5)

    @allure.description('SignUp when UserName & password incorrectly')
    def test_SignUp_with_incorrectly_UserName_and_password(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_password_and_UserName
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 400)
        SignUp.Assert_Elapsed_time(url, data, 5)

    @allure.description('SignUp when UserName & password are null')
    def test_SignUp_with_null_UserName_and_password(self):
        url = Login_Locators.url_login
        data = {}
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 400)
        SignUp.Assert_Elapsed_time(url, data, 10)
