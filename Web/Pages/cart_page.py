import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locator_cart import Locators_CartPage
from Web.Utils.utils import Utils


class Cart_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.cart_option = Locators_CartPage.CART_OPTION
        self.placeOrder_button = Locators_CartPage.PLACE_ORDER_BTN
        self.close_page = Locators_CartPage.CLOSE_BUTTON
        self.title = Locators_CartPage.PAGE_TITLE
        self.cart_url = Locators_CartPage.CART_PAGE_URL
        self.fillOut_name_and_creditcard = Locators_CartPage.FILL_NAME_AND_CREDITCARD
        self.name = Locators_CartPage.NAME
        self.country = Locators_CartPage.COUNTRY
        self.city = Locators_CartPage.CITY
        self.credit_card = Locators_CartPage.CREDIT_CARD
        self.month = Locators_CartPage.MONTH_CARD
        self.year = Locators_CartPage.YEAR_CARD
        self.purchase_button = Locators_CartPage.PURCHASE_BUTTON
        self.ok_conformation = Locators_CartPage.OK_CONFORMATION
        self.delete_product = Locators_CartPage.DELETE_ORDER_LINK

    @allure.step
    @allure.description('Navigate to Main Home page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to homepage and click Cart option')
    def click_Cart_option(self):
        self.driver.find_element(By.XPATH, self.cart_option).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Navigate to CartPage and click Place Order Button')
    def click_PlaceOrder_button(self):
        self.driver.find_element(By.XPATH, self.placeOrder_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)
        time.sleep(2)

    @allure.step
    @allure.description('Navigate to CartPage and click Purchase Order Button')
    def click_Purchase_button(self):
        self.driver.find_element(By.XPATH, self.purchase_button).click()
        time.sleep(5)

    @allure.step
    @allure.description('Navigate to CartPage and click Purchase Order Button')
    def click_Ok_Conformation_button(self):
        self.driver.find_element(By.XPATH, self.ok_conformation).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Check the alert text message "Product added" displayed')
    def Assert_alert_fill_out_Name_and_Creditcard(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.fillOut_name_and_creditcard, alert_text)

    @allure.step
    @allure.description('Click Alert OK button after purchase')
    def click_OK_alert_button(self):
        self.wait.until((EC.alert_is_present()))
        alert = self.driver.switch_to.alert
        alert.accept()

    @allure.step
    @allure.description('Clear and insert data to Name input')
    def enter_Name(self, Name):
        Name_input = self.driver.find_element(By.XPATH, self.name)
        Name_input.clear()
        Name_input.send_keys(Name)
        Utils(self.driver).assertion(Name, Name_input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Country input')
    def enter_Country(self, country):
        country_input = self.driver.find_element(By.XPATH, self.country)
        country_input.clear()
        country_input.send_keys(country)
        Utils(self.driver).assertion(country, country_input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Country input')
    def enter_City(self, City):
        City_input = self.driver.find_element(By.XPATH, self.city)
        City_input.clear()
        City_input.send_keys(City)
        Utils(self.driver).assertion(City, City_input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Credit card input')
    def enter_Credit_card(self, Credit_card):
        Credit_card_input = self.driver.find_element(By.XPATH, self.credit_card)
        Credit_card_input.clear()
        Credit_card_input.send_keys(Credit_card)
        Utils(self.driver).assertion(Credit_card, Credit_card_input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Month card input')
    def enter_Month(self, Month):
        Month_input = self.driver.find_element(By.XPATH, self.month)
        Month_input.clear()
        Month_input.send_keys(Month)
        Utils(self.driver).assertion(Month, Month_input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Month card input')
    def enter_Year(self, Year):
        Year_input = self.driver.find_element(By.XPATH, self.year)
        Year_input.clear()
        Year_input.send_keys(Year)
        Utils(self.driver).assertion(Year, Year_input.get_attribute('value'))

    @allure.step
    @allure.description('Navigate to CartPage and click delete Order Button')
    def click_delete_button(self):
        self.driver.find_element(By.XPATH, self.delete_product).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)
        time.sleep(2)

    @allure.step
    @allure.description('Enter all valid details on order placing form')
    def Enter_All_details_on_placeOrder_Form(self,Name, country, City, Credit_card, Month, Year):
        Name_input = self.driver.find_element(By.XPATH, self.name)
        Name_input.clear()
        Name_input.send_keys(Name)
        Utils(self.driver).assertion(Name, Name_input.get_attribute('value'))
        country_input = self.driver.find_element(By.XPATH, self.country)
        country_input.clear()
        country_input.send_keys(country)
        Utils(self.driver).assertion(country, country_input.get_attribute('value'))
        City_input = self.driver.find_element(By.XPATH, self.city)
        City_input.clear()
        City_input.send_keys(City)
        Utils(self.driver).assertion(City, City_input.get_attribute('value'))
        Credit_card_input = self.driver.find_element(By.XPATH, self.credit_card)
        Credit_card_input.clear()
        Credit_card_input.send_keys(Credit_card)
        Utils(self.driver).assertion(Credit_card, Credit_card_input.get_attribute('value'))
        Month_input = self.driver.find_element(By.XPATH, self.month)
        Month_input.clear()
        Month_input.send_keys(Month)
        Utils(self.driver).assertion(Month, Month_input.get_attribute('value'))
        Year_input = self.driver.find_element(By.XPATH, self.year)
        Year_input.clear()
        Year_input.send_keys(Year)
        Utils(self.driver).assertion(Year, Year_input.get_attribute('value'))

    @allure.step
    @allure.description('successfully order product using place order form')
    def PlaceOrder_successfully(self):
        time.sleep(2)
        self.click_PlaceOrder_button()
        self.driver.implicitly_wait(2)
        self.Enter_All_details_on_placeOrder_Form("David","Israel","Beer-sheva","12345678910","7","2025")
        self.click_Purchase_button()
        self.click_Ok_Conformation_button()
        Utils(self.driver).assertion(self.title, self.driver.title)
