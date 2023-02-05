import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locators_home import Locators_HomePage
from Web.Utils.utils import Utils


class Home_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.home_icon = Locators_HomePage.HOME_OPTION
        self.home_icon2 = Locators_HomePage.HOME_OPTION2
        self.image_logo = Locators_HomePage.IMG_LOGO_ICON
        self.text_logo = Locators_HomePage.TEXT_LOGO_ICON
        self.next_button = Locators_HomePage.NEXT_BUTTON
        self.Prev_button = Locators_HomePage.PREV_BUTTON
        self.footer_next_button = Locators_HomePage.NEXT2_BUTTON_ID
        self.fotter_Prev_button = Locators_HomePage.PREV2_BUTTON_ID
        self.categories_icon = Locators_HomePage.CATEGORIES_ICON
        self.phone_catagory_icon = Locators_HomePage.PHONE_CATEG0RY_ICON
        self.laptop_catagory_icon = Locators_HomePage.LAPTOPS_CATEG0RY_ICON
        self.monitor_catagory_icon = Locators_HomePage.MONITORS_CATEG0RY_ICON
        self.current_url = Locators_HomePage.CURRENT_URL
        self.current_title = Locators_HomePage.CURRENT_TITLE
        self.S6_link = Locators_HomePage.SAMSUNG_GALAXY_S6_LINK
        self.S6_url = Locators_HomePage.S6_URL
        self.MacBook_pro_link = Locators_HomePage.MACBOOK_PRO_LINK
        self.MacBookPro_url = Locators_HomePage.MACBOOK_PRO_URL
        self.apple24_link = Locators_HomePage.APPLE_MONITOR24_LINK
        self.Apple24_url = Locators_HomePage.APPLE_MONITOR24_URL
        self.add_to_cart_button = Locators_HomePage.ADD_TO_CART_BUTTON
        self.Product_add_message = Locators_HomePage.ADD_PRODUCT
        self.Cart_link = Locators_HomePage.CART_LINK
        self.Cart_url = Locators_HomePage.CART_URL

    @allure.step
    @allure.description('Navigate to Main Home page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to brand Image "B" logo after Home page display')
    def click_image_logo_icon(self):
        self.driver.find_element(By.XPATH, self.image_logo).click()
        self.wait.until(EC.url_to_be(self.current_url))
        Utils(self.driver).assertion(self.current_url, self.driver.current_url)

    @allure.step
    @allure.description('Navigate to brand Text logo "PRODUCT STORE" after Home page display')
    def click_Text_logo_icon(self):
        self.driver.find_element(By.XPATH, self.text_logo).click()
        self.wait.until(EC.url_to_be(self.current_url))
        Utils(self.driver).assertion(self.current_url, self.driver.current_url)

    @allure.step
    @allure.description('Navigate to Home icon after Home page display')
    def click_Home_icon(self):
        self.driver.find_element(By.XPATH, self.home_icon).click()
        self.wait.until(EC.url_to_be(self.current_url))
        Utils(self.driver).assertion(self.current_url, self.driver.current_url)

    @allure.step
    @allure.description('Navigate to Home icon after Adding product to cart and click home')
    def click_after_adding_Home_icon(self):
        self.driver.find_element(By.XPATH, self.home_icon2).click()
        self.wait.until(EC.url_to_be(self.current_url))
        Utils(self.driver).assertion(self.current_url, self.driver.current_url)

    @allure.step
    @allure.description('Display product by clicking Next button on the center')
    def click_Next_Button(self):
        self.driver.find_element(By.XPATH, self.next_button).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Display product by clicking Previous button on the center')
    def click_Previous_Button(self):
        self.driver.find_element(By.XPATH, self.next_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))

    @allure.step
    @allure.description('Display product by clicking Next button on the footer')
    def scroll_down(self):
        self.driver.implicitly_wait(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

    @allure.step
    @allure.description('Display product by clicking Next button on the footer')
    def click_fotter_Next_Button(self):
        self.driver.find_element(By.ID, self.footer_next_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))

    @allure.step
    @allure.description('Display product by clicking Previous button on the footer')
    def click_fotter_Previous_Button(self):
        self.driver.find_element(By.ID, self.fotter_Prev_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))

    @allure.step
    @allure.description('Display Monitor product by clicking Monitor category icon')
    def click_categories_icon(self):
        self.driver.find_element(By.XPATH, self.categories_icon).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))

    @allure.step
    @allure.description('Display Phone product by clicking phone category icon')
    def click_phone_category_icon(self):
        self.driver.find_element(By.XPATH, self.phone_catagory_icon).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))

    @allure.step
    @allure.description("Add the product to Cart from phone categories")
    def click_on_S6_phone(self):
        self.driver.find_element(By.XPATH, self.S6_link).click()
        self.wait.until(EC.url_to_be(self.S6_url))

    @allure.step
    @allure.description('Display Laptop product by clicking Laptop category icon')
    def click_laptop_category_icon(self):
        self.driver.find_element(By.XPATH, self.laptop_catagory_icon).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))

    @allure.step
    @allure.description("Add the product to Cart from Laptop categories")
    def Click_on_MacBook_pro_laptop(self):
        self.driver.find_element(By.XPATH, self.MacBook_pro_link).click()
        self.wait.until(EC.url_to_be(self.MacBookPro_url))

    @allure.step
    @allure.description('Display Monitor product by clicking Monitor category icon')
    def click_Monitors_category_icon(self):
        self.driver.find_element(By.XPATH, self.monitor_catagory_icon).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))

    @allure.step
    @allure.description("Add the product to Cart from Monitor categories")
    def click_on_Apple24_monitor(self):
        self.driver.find_element(By.XPATH, self.apple24_link).click()
        self.wait.until(EC.url_to_be(self.Apple24_url))

    @allure.step
    @allure.description('Navigate to Add to cart and add product to the cart')
    def click_Add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_button).click()
        time.sleep(2)

    @allure.step
    @allure.description('Check the alert text message "Product added" displayed')
    def Assert_alert_Product_added(self):
        alert_text = self.driver.switch_to.alert.text
        print("\nAlert message = ", alert_text, "\n")
        Utils(self.driver).assertion(self.Product_add_message, alert_text)

    @allure.step
    @allure.description('Click Alert OK button after click product added')
    def click_OK_alert_button(self):
        self.wait.until((EC.alert_is_present()))
        alert = self.driver.switch_to.alert
        alert.accept()

    @allure.step
    @allure.description('Click cart option and check all product are added')
    def Click_Cart_Option(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Cart_link).click()
        time.sleep(2)

    @allure.step
    @allure.description('Add All Phone Products Using FOR loop')
    def ADD_all_phone_products(self):
        Count = 0
        for item in range(7):
            self.click_phone_category_icon()
            self.driver.implicitly_wait(2)
            time.sleep(2)
            self.driver.find_element(By.XPATH, f"/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[{Count+1}]/div[1]/a[1]/img[1]").click()
            self.click_Add_to_cart_button()
            self.Assert_alert_Product_added()
            self.click_OK_alert_button()
            self.driver.implicitly_wait(2)
            self.driver.back()
            self.driver.back()
            Count += 1

    @allure.step
    @allure.description('Add All Laptop Products Using FOR loop')
    def ADD_all_Laptop_products(self):
        Count = 0
        for item in range(6):
            self.click_laptop_category_icon()
            self.driver.implicitly_wait(2)
            time.sleep(2)
            self.driver.find_element(By.XPATH,f"/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[{Count+1}]/div[1]/div[1]/h4[1]/a[1]").click()
            self.click_Add_to_cart_button()
            self.Assert_alert_Product_added()
            self.click_OK_alert_button()
            self.driver.implicitly_wait(2)
            self.driver.back()
            self.driver.back()
            Count += 1

    @allure.step
    @allure.description('Add All Monitor Products Using FOR loop')
    def ADD_all_Monitor_products(self):
        Count = 0
        for item in range(2):
            self.click_Monitors_category_icon()
            self.driver.implicitly_wait(2)
            time.sleep(2)
            self.driver.find_element(By.XPATH,
                                     f"/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[{Count+1}]/div[1]/div[1]/h4[1]/a[1]").click()
            self.click_Add_to_cart_button()
            self.Assert_alert_Product_added()
            self.click_OK_alert_button()
            self.driver.implicitly_wait(2)
            self.driver.back()
            self.driver.back()
            Count += 1
