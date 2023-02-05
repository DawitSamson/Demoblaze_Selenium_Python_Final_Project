import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locators_login import Locators_Login
from Web.Utils.utils import Utils


class Login_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.title = Locators_Login.PAGE_TITLE
        self.login_option = Locators_Login.LOGIN_OPTION
        self.userName = Locators_Login.USERNAME
        self.password = Locators_Login.PASSWORD
        self.x_button = Locators_Login.X_BUTTON
        self.login_button = Locators_Login.LOGIN_BUTTON
        self.close_page_button = Locators_Login.CLOSE_BUTTON
        self.fill_error_text1 = Locators_Login.ERROR_TEXT1
        self.wrong_text = Locators_Login.WRONG_PASSWORD
        self.welcome_text = Locators_Login.WELCOME_TEXT
        self.user_not_exist = Locators_Login.USER_NOT_EXISTS

    @allure.step
    @allure.description('Navigate to Main Home page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to Login page after Home page display')
    def click_Login_option(self):
        self.driver.find_element(By.XPATH, self.login_option).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)
        self.driver.implicitly_wait(2)

    @allure.step
    @allure.description('Clear and insert data to UserName input')
    def enter_UserName(self, UserName):
        UserName_Input = self.driver.find_element(By.XPATH, self.userName)
        UserName_Input.clear()
        UserName_Input.send_keys(UserName)
        Utils(self.driver).assertion(UserName, UserName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Password input')
    def enter_Password(self, Password):
        Password_input = self.driver.find_element(By.XPATH, self.password)
        Password_input.clear()
        Password_input.send_keys(Password)
        Utils(self.driver).assertion(Password, Password_input.get_attribute('value'))

    @allure.step
    @allure.description('Click signUp button to register on the website')
    def click_Login_Button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(5)

    @allure.step
    @allure.description('Click Close button to Close Login page')
    def click_Close_Button(self):
        self.driver.find_element(By.XPATH, self.close_page_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click X button to to Close Login page')
    def click_X_Button(self):
        self.driver.find_element(By.XPATH, self.close_page_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Check the alert text message "Please fill out Username and Password." displayed')
    def Assert_alert_fill_error(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.fill_error_text1, alert_text)

    @allure.step
    @allure.description('Check the alert text message "Wrong password." displayed')
    def Assert_alert_wrong_password(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.wrong_text, alert_text)

    @allure.step
    @allure.description('Check the alert text message "User does not exist." displayed')
    def Assert_alert_User_Not_exist(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.user_not_exist, alert_text)

    @allure.step
    @allure.description('Click Alert OK button after click login')
    def click_OK_alert_button(self):
        self.wait.until((EC.alert_is_present()))
        alert = self.driver.switch_to.alert
        alert.accept()
