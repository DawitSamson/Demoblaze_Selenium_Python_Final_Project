import allure
import requests


class SignUp_Page:

    @allure.step
    @allure.description("test status code need to be 200")
    def Assert_Status_code(self, URL, DATA, Status_Code):
        Req = requests.post(URL, json=DATA)
        assert Req.status_code == Status_Code
        print("\nActual Status code=", Req.status_code, "\nExpected Status code=", Status_Code)

    @allure.step
    @allure.description("the time elapse for the test takes < given seconds")
    def Assert_Elapsed_time(self, URL, DATA, Second):
        Req = requests.post(URL, json=DATA)
        assert Req.elapsed.total_seconds() < Second
        print("\nActual Elapsed time=", Req.elapsed.total_seconds(), "\nExpected Elapsed time=", Second)
