from API.locators_Api.login_locators import Login_Locators
import allure
import pytest
from API.Pages_Api.login_page import Login_Page


class Test_Login(Login_Page):
    @allure.description('Login correctly using Valid UserName and Password')
    @pytest.mark.sanity
    def test_login_correctly(self):
        url = Login_Locators.url_login
        data = Login_Locators.valid_UserName_and_password
        login = Login_Page()
        login.Assert_Status_code(url, data, 200)
        login.Assert_Elapsed_time(url, data, 5)  # less than the given second

    @allure.description('Login when password incorrectly')
    def test_login_with_incorrectly_password(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_password
        login = Login_Page()
        login.Assert_Status_code(url, data, 400)
        login.Assert_Elapsed_time(url, data, 5)

    @allure.description('Login when UserName incorrectly')
    def test_login_with_incorrectly_UserName(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_UserName
        login = Login_Page()
        login.Assert_Status_code(url, data, 400)
        login.Assert_Elapsed_time(url, data, 5)

    @allure.description('Login when UserName & password incorrectly')
    def test_login_with_incorrectly_UserName_and_password(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_password_and_UserName
        login = Login_Page()
        login.Assert_Status_code(url, data, 400)
        login.Assert_Elapsed_time(url, data, 5)

    @allure.description('Login when UserName & password are null')
    def test_login_with_null_UserName_and_password(self):
        url = Login_Locators.url_login
        data = {}
        login = Login_Page()
        login.Assert_Status_code(url, data, 400)
        login.Assert_Elapsed_time(url, data, 5)
