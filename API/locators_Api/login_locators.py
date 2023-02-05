class Login_Locators:
    url_login = 'https://api.demoblaze.com/login'
    Error_message = 'Please fill out Username and Password.'
    valid_UserName_and_password = {"Username:": "Dawit", "password:": "123456"}
    Invalid_password = {"Username:": "Dawit", "password:": "2023"}
    Invalid_UserName = {"Username:": "Dawwwwww", "password:": "123456"}
    Invalid_password_and_UserName = {"Username:": "Dawwwww", "password:": "2023"}
