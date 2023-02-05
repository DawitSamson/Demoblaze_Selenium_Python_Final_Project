import allure
import pytest
from Web.Pages.cart_page import Cart_Page
from Web.Pages.home_page import Home_Page
from Web.Utils.utils import Utils
from Web.Base.base_test import Base_Page


class Test_Cart(Base_Page):

    @allure.description('Successfully Display DemoBlaze Cart page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Cart_page_from_Header_Cart_options(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()

    @allure.description('Successfully place order after Product added to cart frome Phone Categories')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_filling_all_valid_detail_by_adding_product_From_Phone_categories_to_Cart(self):
        driver = self.driver
        cart = Cart_Page(driver)
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_phone_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.click_on_S6_phone()
        home.click_Add_to_cart_button()
        home.Assert_alert_Product_added()
        home.click_OK_alert_button()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        Utils(driver).assertion(cart.title,self.driver.title)
        cart.Enter_All_details_on_placeOrder_Form("David", "Israel", "Beer-sheva", "12345678910", "12", "2025")
        cart.click_Purchase_button()
        cart.click_Ok_Conformation_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully place order with out adding product to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_filling_all_valid_detail_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.Enter_All_details_on_placeOrder_Form("David", "Israel", "Beer-sheva", "12345678910", "12", "2025")
        cart.click_Purchase_button()
        cart.click_Ok_Conformation_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully delete added product from cart page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Delete_added_product_to_cart_button_using_delete_button(self):
        driver = self.driver
        cart = Cart_Page(driver)
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_phone_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.click_on_S6_phone()
        home.click_Add_to_cart_button()
        home.Assert_alert_Product_added()
        home.click_OK_alert_button()
        cart.click_Cart_option()
        cart.click_delete_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Place order by not filling the valid detail values and receive alert message "Please fill out Name and Creditcard."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_not_filling_all_valid_detail_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.click_Purchase_button()
        cart.Assert_alert_fill_out_Name_and_Creditcard()
        cart.click_OK_alert_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Place order by not filling the valid detail values and receive alert message "Please fill out Name and Creditcard."')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_not_filling_all_valid_detail_with_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        home = Home_Page(driver)
        home.open_Main_page()
        home.click_phone_category_icon()
        Utils(driver).assertion(home.current_title, self.driver.title)
        home.click_on_S6_phone()
        home.click_Add_to_cart_button()
        home.Assert_alert_Product_added()
        home.click_OK_alert_button()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        Utils(driver).assertion(cart.title, self.driver.title)
        cart.click_Purchase_button()
        cart.Assert_alert_fill_out_Name_and_Creditcard()
        cart.click_OK_alert_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully place order using blank name and with out adding product to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_Not_Filling_Name_detail_and_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.enter_Name("")
        cart.enter_Country("Israel")
        cart.enter_City("Beer-sheva")
        cart.enter_Credit_card("147258369")
        cart.enter_Month("12")
        cart.enter_Year("2025")
        cart.click_Purchase_button()
        cart.Assert_alert_fill_out_Name_and_Creditcard()
        cart.click_OK_alert_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully place order using blank Country and with out adding product to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_Not_Filling_Country_detail_and_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.enter_Name("David")
        cart.enter_Country("")
        cart.enter_City("Beer-sheva")
        cart.enter_Credit_card("147258369")
        cart.enter_Month("12")
        cart.enter_Year("2025")
        cart.click_Purchase_button()
        cart.click_Ok_Conformation_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully place order using blank City and with out adding product to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_Not_Filling_City_detail_and_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.enter_Name("David")
        cart.enter_Country("Israel")
        cart.enter_City("")
        cart.enter_Credit_card("147258369")
        cart.enter_Month("12")
        cart.enter_Year("2025")
        cart.click_Purchase_button()
        cart.click_Ok_Conformation_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully place order using blank Credit-Card and with out adding product to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_Not_Filling_Credit_Card_detail_and_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.enter_Name("David")
        cart.enter_Country("Israel")
        cart.enter_City("Beer-sheva")
        cart.enter_Credit_card("")
        cart.enter_Month("12")
        cart.enter_Year("2025")
        cart.click_Purchase_button()
        cart.Assert_alert_fill_out_Name_and_Creditcard()
        cart.click_OK_alert_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully place order using blank Month and with out adding product to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_Not_Filling_Month_detail_and_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.Enter_All_details_on_placeOrder_Form("David", "Israel", "Beer-sheva", "12345678910", "", "2025")
        cart.click_Purchase_button()
        cart.click_Ok_Conformation_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully place order using blank City and with out adding product to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_Not_Filling_Year_detail_and_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.Enter_All_details_on_placeOrder_Form("David", "Israel", "Beer-sheva", "12345678910", "12", "")
        cart.click_Purchase_button()
        cart.click_Ok_Conformation_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    @allure.description('Successfully place order using blank City and with out adding product to cart')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_Place_Order_by_Not_Filling_Year_and_Month_detail_and_without_adding_any_product(self):
        driver = self.driver
        cart = Cart_Page(driver)
        cart.open_Main_page()
        cart.click_Cart_option()
        cart.click_PlaceOrder_button()
        cart.Enter_All_details_on_placeOrder_Form("David", "Israel", "Beer-sheva", "12345678910", "", "")
        cart.click_Purchase_button()
        cart.click_Ok_Conformation_button()
        Utils(driver).assertion(cart.title, self.driver.title)

    # This is the over purchasing of all product from selecting all product to receiving Conformation Code.
    @allure.description('Successfully Purchase all product using valid details')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Purchase_all_Product_Using_valid_details(self):
        driver = self.driver
        home_E2E = Home_Page(driver)
        home_E2E.open_Main_page()
        home_E2E.click_Home_icon()
        home_E2E.ADD_all_phone_products()
        home_E2E.ADD_all_Laptop_products()
        home_E2E.ADD_all_Monitor_products()
        cart_E2E = Cart_Page(driver)
        cart_E2E.click_Cart_option()
        cart_E2E.PlaceOrder_successfully()
