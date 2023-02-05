import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locators_signUp import Locators_SignUp
from Web.Utils.utils import Utils


class SignUp_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.title = Locators_SignUp.PAGE_TITLE
        self.signUp_option = Locators_SignUp.SIGNUP_OPTION
        self.userName = Locators_SignUp.USERNAME
        self.password = Locators_SignUp.PASSWORD
        self.x_button = Locators_SignUp.X_BUTTON
        self.signup_button = Locators_SignUp.SIGNUP_BUTTON
        self.close_page_button = Locators_SignUp.CLOSE_BUTTON
        self.error_text1 = Locators_SignUp.ERROR_TEXT1
        self.success_text = Locators_SignUp.SUCCESS_TEXT
        self.exist_text = Locators_SignUp.EXIST_TEXT

    @allure.step
    @allure.description('Navigate to Main Home page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to SignUp page after Home page display')
    def click_SignUp_option(self):
        self.driver.find_element(By.XPATH, self.signUp_option).click()
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
    def click_SignUp_Button(self):
        self.driver.find_element(By.XPATH, self.signup_button).click()
        time.sleep(5)

    @allure.step
    @allure.description('Click X button to to Close SignUp page')
    def click_X_Button(self):
        self.driver.find_element(By.XPATH, self.x_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click Close button to Close SignUp page')
    def click_Close_Button(self):
        self.driver.find_element(By.XPATH, self.close_page_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Check the alert text message "Please fill out Username and Password." displayed')
    def Assert_alert_fill_error(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.error_text1, alert_text)

    @allure.step
    @allure.description('Check the alert text message "Sign up successful." displayed')
    def Assert_alert_success_text1(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.success_text, alert_text)

    @allure.step
    @allure.description('Check the alert text message "This user already exist." displayed')
    def Assert_alert_exist_text1(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.exist_text, alert_text)

    @allure.step
    @allure.description('Click Alert OK button after click signup successfully')
    def click_OK_alert_button(self):
        self.wait.until((EC.alert_is_present()))
        alert = self.driver.switch_to.alert
        alert.accept()
