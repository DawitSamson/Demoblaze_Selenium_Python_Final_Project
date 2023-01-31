from API.Constants.login_constants import Login_Constants
import allure
import requests


class Test_Login:
    @allure.description('Login correctly')
    @allure.step("test status code need to be 200")
    @allure.step("the time elapse for the test takes < 10 seconds ")
    def test_login_correctly(self):
        url = Login_Constants.url_login
        data = Login_Constants.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data[Login_Constants.success_key] == True
        assert res_data[Login_Constants.message_key] == 'login successful'

    @allure.description('Login when password incorrectly')
    def test_login_with_incorrectly_password(self):
        url = Login_Constants.url_login
        data = Login_Constants.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[Login_Constants.success_key] == False
        assert res_data[Login_Constants.message_key] == "password or email incorrect"

    @allure.description('Login when email incorrectly')
    def test_login_with_incorrectly_email(self):
        url = Login_Constants.url_login
        data = Login_Constants.data_invalid_email
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[Login_Constants.success_key] == False
        assert res_data[Login_Constants.message_key] == "no user found"

    @allure.description('Login when email & password incorrectly')
    def test_login_with_incorrectly_email_and_password(self):
        url = Login_Constants.url_login
        data = Login_Constants.data_invalid_password_and_email
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[Login_Constants.success_key] == False
        assert res_data[Login_Constants.message_key] == "no user found"

    @allure.description('Login when email & password are null')
    def test_login_with_null_email_and_password(self):
        url = Login_Constants.url_login
        data = {}
        res = requests.post(url, data=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[Login_Constants.success_key] == False
        assert res_data[Login_Constants.message_key] == 'no user found'




