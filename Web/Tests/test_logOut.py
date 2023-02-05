import allure
import pytest
from Web.Pages.logOut_page import LogOut_page
from Web.Base.base_test import Base_Page
from Web.Pages.login_page import Login_Page
from Web.Utils.utils import Utils


class Test_SignUp(Base_Page):

    @allure.description('Successfully Logout while clicking logout ')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Logout_from_the_login_account_by_Clicking_Logout(self):
        driver = self.driver
        logout = LogOut_page(driver)
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Login_option()
        login.enter_UserName("dawit")
        login.enter_Password("12345")
        login.click_Login_Button()
        Utils(driver).assertion(logout.title, self.driver.title)
        logout.click_LogOut_option()
        Utils(driver).assertion(logout.title, self.driver.title)
