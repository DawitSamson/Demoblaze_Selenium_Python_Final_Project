import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locators_contact import Locators_ContactPage
from Web.Utils.utils import Utils


class Contact_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.contact_option = Locators_ContactPage.CONTACT_OPTION
        self.email_box = Locators_ContactPage.EMAIL_BOX
        self.name_box = Locators_ContactPage.NAME_BOX
        self.message_box = Locators_ContactPage.MESSAGE_BOX
        self.send_button = Locators_ContactPage.SEND_BUTTON
        self.close_button = Locators_ContactPage.CLOSE_BUTTON
        self.contact_url = Locators_ContactPage.CONTACT_CURRENT_URL
        self.title = Locators_ContactPage.PAGE_TITLE
        self.newMessage_id = Locators_ContactPage.NEW_MESSAGE_ID
        self.thankyou_message = Locators_ContactPage.THANKYOU_MESSAGE
        self.ERROR_TEXT = Locators_ContactPage.ERROR_TEXT1

    @allure.step
    @allure.description('Navigate to Main Home page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to homepage and click Contact option')
    def click_Contact_option(self):
        self.driver.find_element(By.XPATH, self.contact_option).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Clear and insert data to email input')
    def enter_email(self, email):
        email_input = self.driver.find_element(By.XPATH, self.email_box)
        email_input.clear()
        email_input.send_keys(email)
        Utils(self.driver).assertion(email, email_input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to name input')
    def enter_name(self, name):
        name_input = self.driver.find_element(By.XPATH, self.name_box)
        name_input.clear()
        name_input.send_keys(name)
        Utils(self.driver).assertion(name, name_input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to massage input')
    def enter_text_message(self, message):
        message_input = self.driver.find_element(By.XPATH, self.message_box)
        message_input.clear()
        message_input.send_keys(message)
        Utils(self.driver).assertion(message, message_input.get_attribute('value'))

    @allure.step
    @allure.description('Click send message Button')
    def click_Send_Message(self):
        self.driver.find_element(By.XPATH, self.send_button).click()
        time.sleep(2)

    @allure.step
    @allure.description('Click Cancel option')
    def click_Close_button(self):
        self.driver.find_element(By.XPATH, self.close_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Check the alert text message "Thanks for the message!!" displayed')
    def Assert_alert_ThankYou_message(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.thankyou_message, alert_text)

    @allure.step
    @allure.description('Click Alert OK button after send message successfully')
    def click_OK_alert_button(self):
        self.wait.until((EC.alert_is_present()))
        alert = self.driver.switch_to.alert
        alert.accept()

    # this is the error message need to be displayed when we make invalid input
    @property
    @allure.step
    @allure.description('Check the alert text message "Please fill out properly." displayed')
    def Assert_alert_Error_message(self):
        return self.driver.switch_to.alert.text
