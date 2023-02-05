import allure
import pytest
from Web.Pages.contact_page import Contact_Page
from Web.Utils.utils import Utils
from Web.Base.base_test import Base_Page


class Test_Contact(Base_Page):

    @allure.description('Successfully Display Contact page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Contact_page_from_Header_Contact_options(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()

    @allure.description('Successfully send message from the contact page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_the_Contact_Form_in_Contact_page_by_providing_all_valid_details(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.enter_email("dcena06@gmail.com")
        contact.enter_name("david")
        contact.enter_text_message("checking the test message field is accepting this message")
        contact.click_Send_Message()
        contact.Assert_alert_ThankYou_message()
        contact.click_OK_alert_button()
        Utils(driver).assertion(contact.title, self.driver.title)

    @allure.description('Successfully Display Home page by clicking close button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.MINOR)
    def test_Validate_Close_button_from_contact_page(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.click_Close_button()
        Utils(driver).assertion(contact.title, self.driver.title)

    @allure.description('Display Error message for not providing the details')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_submitting_the_Contact_Form_in_Contact_page_by_not_providing_any_details(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.click_Send_Message()
        alert_text = contact.Assert_alert_Error_message
        assert alert_text == contact.ERROR_TEXT
        contact.click_OK_alert_button()
        Utils(driver).assertion(contact.title, self.driver.title)

    @allure.description('Display Error message for not providing the details')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_entering_invalid_email_address_into_the_EMail_Address_field_and_submit_the_form(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.enter_email("dcena06@")
        contact.enter_name("david")
        contact.enter_text_message("test message field")
        contact.click_Send_Message()
        alert_text = contact.Assert_alert_Error_message
        assert alert_text == contact.ERROR_TEXT
        contact.click_OK_alert_button()
        Utils(driver).assertion(contact.title, self.driver.title)

    @allure.description('Display Error message for not providing the details')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_entering_blank_Name_into_the_Name_field_and_submit_the_form(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.enter_email("dcena06@gmail.com")
        contact.enter_name("")
        contact.enter_text_message("test message field")
        contact.click_Send_Message()
        alert_text = contact.Assert_alert_Error_message
        assert alert_text == contact.ERROR_TEXT
        contact.click_OK_alert_button()
        Utils(driver).assertion(contact.title, self.driver.title)

    @allure.description('Display Error message for not providing the details')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_entering_blank_Message_into_the_Message_field_and_submit_the_form(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.enter_email("dcena06@gmail.com")
        contact.enter_name("david")
        contact.enter_text_message("")
        contact.click_Send_Message()
        alert_text = contact.Assert_alert_Error_message
        assert alert_text == contact.ERROR_TEXT
        contact.click_OK_alert_button()
        Utils(driver).assertion(contact.title, self.driver.title)

    @allure.description('Display Error message for not providing the details')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_entering_Special_Characters_email_address_into_the_EMail_Address_field_and_submit_the_form(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.enter_email("!@!@!@")
        contact.enter_name("david")
        contact.enter_text_message("test message field")
        contact.click_Send_Message()
        alert_text = contact.Assert_alert_Error_message
        assert alert_text == contact.ERROR_TEXT
        contact.click_OK_alert_button()
        Utils(driver).assertion(contact.title, self.driver.title)

    @allure.description('Display Error message for not providing the details')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_entering_Special_Characters_Name_into_the_Name_field_and_submit_the_form(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.enter_email("dcena06@gmail.com")
        contact.enter_name("!@#$%")
        contact.enter_text_message("test message field")
        contact.click_Send_Message()
        alert_text = contact.Assert_alert_Error_message
        assert alert_text == contact.ERROR_TEXT
        contact.click_OK_alert_button()
        Utils(driver).assertion(contact.title, self.driver.title)

    @allure.description('Display Error message for not providing the details')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_entering_Special_Characters_Message_into_the_Message_field_and_submit_the_form(self):
        driver = self.driver
        contact = Contact_Page(driver)
        contact.open_Main_page()
        contact.click_Contact_option()
        contact.enter_email("dcena06@gmail.com")
        contact.enter_name("david")
        contact.enter_text_message("!@#$%^&*()_)(*&^%$#@!@#$%^&*()_+_)(*&^%$#")
        contact.click_Send_Message()
        alert_text = contact.Assert_alert_Error_message
        assert alert_text == contact.ERROR_TEXT
        contact.click_OK_alert_button()
        Utils(driver).assertion(contact.title, self.driver.title)
