import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locators_aboutUs import Locators_AboutUs
from Web.Utils.utils import Utils


class AboutUs_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.aboutUs_option = Locators_AboutUs.ABOUTUS_OPTION
        self.close_button = Locators_AboutUs.PAGE_CLOSE_BUTTON
        self.play_video_button = Locators_AboutUs.PLAY_VIDEO_BUTTON
        self.play_video_image = Locators_AboutUs.PLAY_VIDEO_IMAGE
        self.x_icon = Locators_AboutUs.X_ICON
        self.play_Pause_button = Locators_AboutUs.PLAY_ICON
        self.fullScreen_button = Locators_AboutUs.FULLSCREEN_ICON
        self.picSize_button = Locators_AboutUs.PIC_SIZE_ICON
        self.mute_button = Locators_AboutUs.MUTE_ICON
        self.title = Locators_AboutUs.PAGE_TITLE

    @allure.step
    @allure.description('Navigate to Main Home page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to homepage and click AboutUs option to display the page')
    def click_About_option(self):
        self.driver.find_element(By.XPATH, self.aboutUs_option).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click AboutUs Page Close Button to close the page')
    def click_Close_button(self):
        self.driver.find_element(By.XPATH, self.close_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click AboutUs Page x icon to close the page')
    def click_X_icon(self):
        self.driver.find_element(By.XPATH, self.close_button).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click AboutUs Page "play video button" to display aboutUs page video')
    def click_Video_Button(self):
        self.driver.find_element(By.XPATH, self.play_video_button).click()
        time.sleep(5)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click AboutUs Page "play video button" to display aboutUs page video')
    def click_PlayVideo_Image(self):
        self.driver.find_element(By.XPATH, self.play_video_image).click()
        time.sleep(5)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click "Pause button" to pause aboutUs page video')
    def click_Pause_Button(self):
        self.driver.find_element(By.XPATH, self.play_Pause_button).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click "Play button" to play aboutUs page video')
    def click_Play_Button(self):
        self.driver.find_element(By.XPATH, self.play_Pause_button).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click "Mute video button" to Mute aboutUs page video')
    def click_Mute_Button(self):
        self.driver.find_element(By.XPATH, self.mute_button).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click "UnMute video button" to UnMute aboutUs page video')
    def click_UnMute_Button(self):
        self.driver.find_element(By.XPATH, self.mute_button).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click "full-screen video button" to Maximise aboutUs page video')
    def click_FullScreen_Button(self):
        self.driver.find_element(By.XPATH, self.fullScreen_button).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click "Non-full-screen video button" to Minimize aboutUs page video')
    def click_NonFullScreen_Button(self):
        self.driver.find_element(By.XPATH, self.fullScreen_button).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description('Click "Picture in picture button" to make picture in picture on aboutUs page video')
    def click_Pic_in_pic_Button(self):
        self.driver.find_element(By.XPATH, self.picSize_button).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)

    @allure.step
    @allure.description(
        'Click "ExitPicture in picture button" to exist picture in picture display on aboutUs page video')
    def click_Exit_Pic_in_pic_Button(self):
        self.driver.find_element(By.XPATH, self.picSize_button).click()
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title, self.driver.title)
