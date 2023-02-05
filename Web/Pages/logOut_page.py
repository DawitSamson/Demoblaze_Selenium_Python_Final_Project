from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locators_logOut import Locators_LogOut
from Web.Utils.utils import Utils


class LogOut_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.title = Locators_LogOut.PAGE_TITLE
        self.logout_option = Locators_LogOut.LOGOUT_OPTION
        self.welcome_text = Locators_LogOut.WELCOME_TEXT

    @allure.step
    @allure.description('Navigate to logout page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to Logout page after Successfully login and click to logout')
    def click_LogOut_option(self):
        self.driver.find_element(By.XPATH, self.logout_option).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)
        self.driver.implicitly_wait(2)

    @allure.step
    @allure.description('Navigate to Logout page after Successfully login and click welcome text')
    def click_Welcome(self):
        self.driver.find_element(By.XPATH, self.welcome_text).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)
        self.driver.implicitly_wait(2)
