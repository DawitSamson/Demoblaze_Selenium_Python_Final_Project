import allure
import pytest
from Web.Pages.home_page import Home_Page
from Web.Utils.utils import Utils
from Web.Base.base_test import Base_Page


class Test_home(Base_Page):

    @allure.description('Successfully Display DemoBlaze home page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_validate_display_DemoBlaze_home_page(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()

    @allure.description('Display DemoBlaze Homepage after Clicking brand Image logo')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Homepage_from_imageLogo(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_image_logo_icon()

    @allure.description('Display DemoBlaze Homepage after Clicking brand Text logo')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Homepage_from_Text_Logo(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_Text_logo_icon()

    @allure.description('Display DemoBlaze Homepage after Clicking Home Icon')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Homepage_from_Home_icon(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_Home_icon()

    @allure.description('Display Product from the home page through Next and Previous button on the center')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_the_product_using_Next_and_Previous_Button_on_Center(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_Next_Button()
        home.click_Previous_Button()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Display Product from the HomePage through Next and Previous button on the Footer')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_the_product_using_Next_and_Previous_Button_on_footer(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.scroll_down()
        home.click_fotter_Next_Button()
        home.click_fotter_Previous_Button()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Display all Products from the Categories by click Catagory button')  # no-std
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Categories_displayed_all_Product_on_home_Display_Page(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_categories_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Display Phones Products from the Phone Categories ')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Categories_Phone_displayed_Product_of_different_models_of_Phones_on_home_Display_Page(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_phone_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Display Laptops Products from the Laptops Categories')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Categories_Laptops_displayed_Product_of_different_models_of_Laptops_on_home_Display_Page(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_laptop_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Display Monitors Products from the Monitors Categories')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Categories_Monitors_displayed_Product_of_different_models_of_Monitors_on_home_Display_Page(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_Monitors_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Add Product to cart from Phone catagory to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Product_Add_to_Cart_from_phone_categories(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_Home_icon()
        home.click_phone_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.click_on_S6_phone()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.click_Add_to_cart_button()
        home.Assert_alert_Product_added()
        home.click_OK_alert_button()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Add Product to cart from Laptop catagory to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Product_Add_to_Cart_from_laptop_categories(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_Home_icon()
        home.click_laptop_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.Click_on_MacBook_pro_laptop()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.click_Add_to_cart_button()
        home.Assert_alert_Product_added()
        home.click_OK_alert_button()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Add Product to cart from Monitor catagory to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Product_Add_to_Cart_from_Monitor_categories(self):
        driver = self.driver
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_Home_icon()
        home.click_Monitors_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.click_on_Apple24_monitor()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.click_Add_to_cart_button()
        home.Assert_alert_Product_added()
        home.click_OK_alert_button()
        Utils(driver).assertion(home.current_title, self.driver.title)

    @allure.description('Add All Product to cart from All catagory to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_E2E_Valid_All_Products_Add_to_Cart_from_All_categories(self):
        driver = self.driver
        E2E = Home_Page(driver)
        E2E.open_Main_page()
        E2E.click_Home_icon()
        E2E.ADD_all_phone_products()
        E2E.ADD_all_Laptop_products()
        E2E.ADD_all_Monitor_products()
        E2E.Click_Cart_Option()
        Utils(driver).assertion(E2E.current_title, self.driver.title)
