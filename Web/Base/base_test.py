import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromService
from selenium import webdriver


class Base_Page:
    driver = None

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(service=ChromService(ChromeDriverManager().install()))
        self.driver.get("https://www.demoblaze.com/")
        print("-----------------------------------------")
        print("Tests is started")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()
