import allure
import pytest
from Web.Pages.aboutUs_page import AboutUs_Page
from Web.Utils.utils import Utils
from Web.Base.base_test import Base_Page


class Test_AboutUs(Base_Page):

    @allure.description('Successfully Display AboutUs page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_AboutUs_page_from_Header_About_Us_options(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()

    @allure.description('Successfully Close AboutUs page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_aboutUs_page_using_close_button(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()
        aboutUs.click_Close_button()
        Utils(self.driver).assertion(aboutUs.title, self.driver.title)

    @allure.description('Successfully Close AboutUs page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_aboutUs_page_using_X_icon(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()
        aboutUs.click_X_icon()
        Utils(self.driver).assertion(aboutUs.title, self.driver.title)

    @allure.description('Successfully Play AboutUs video using play video button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Play_Video_of_aboutUs_page_by_clicking_play_Video_button(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()
        aboutUs.click_Video_Button()
        Utils(self.driver).assertion(aboutUs.title, self.driver.title)

    @allure.description('Successfully Play AboutUs video using play image')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Play_Video_of_aboutUs_page_by_clicking_Video_Image(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()
        aboutUs.click_PlayVideo_Image()
        aboutUs.click_Close_button()
        Utils(self.driver).assertion(aboutUs.title, self.driver.title)

    @allure.description('Successfully Play AboutUs video using play video button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Pause_Video_of_aboutUs_page_by_clicking_Pause_Video_button(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()
        aboutUs.click_Video_Button()
        aboutUs.click_Pause_Button()
        aboutUs.click_Play_Button()
        Utils(self.driver).assertion(aboutUs.title, self.driver.title)

    @allure.description('Successfully Mute AboutUs video using mute video button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Mute_Video_of_aboutUs_page_by_clicking_Mute_Video_button(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()
        aboutUs.click_Video_Button()
        aboutUs.click_Mute_Button()
        aboutUs.click_UnMute_Button()
        Utils(self.driver).assertion(aboutUs.title, self.driver.title)

    @allure.description('Successfully FullScreen AboutUs video using FullScreen video button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_FullScreen_Video_of_aboutUs_page_by_clicking_FullScreen_Video_button(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()
        aboutUs.click_Video_Button()
        aboutUs.click_FullScreen_Button()
        aboutUs.click_NonFullScreen_Button()
        Utils(self.driver).assertion(aboutUs.title, self.driver.title)

    @allure.description('Successfully PictureSize AboutUs video using PictureSize video button')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_PictureSize_Video_of_aboutUs_page_by_clicking_PictureSize_Video_button(self):
        driver = self.driver
        aboutUs = AboutUs_Page(driver)
        aboutUs.open_Main_page()
        aboutUs.click_About_option()
        aboutUs.click_Video_Button()
        aboutUs.click_Pic_in_pic_Button()
        aboutUs.click_Exit_Pic_in_pic_Button()
        Utils(self.driver).assertion(aboutUs.title, self.driver.title)

    @allure.description('Successfully Play video using All modules')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_E2E_aboutUs_page_video_Playing_using_all_Modules(self):
        driver = self.driver
        aboutUs_E2E = AboutUs_Page(driver)
        aboutUs_E2E.open_Main_page()
        aboutUs_E2E.click_About_option()
        aboutUs_E2E.click_Video_Button()
        aboutUs_E2E.click_Pause_Button()
        aboutUs_E2E.click_Play_Button()
        aboutUs_E2E.click_Mute_Button()
        aboutUs_E2E.click_UnMute_Button()
        aboutUs_E2E.click_Pic_in_pic_Button()
        aboutUs_E2E.click_Exit_Pic_in_pic_Button()
        aboutUs_E2E.click_FullScreen_Button()
        aboutUs_E2E.click_NonFullScreen_Button()
        aboutUs_E2E.click_Close_button()
        Utils(self.driver).assertion(aboutUs_E2E.title, self.driver.title)
