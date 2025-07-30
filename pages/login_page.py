from playwright.sync_api import Page, expect
import allure

class LoginPage:

    def __init__(self, page: Page, ) -> None:
        self.__page = page
        self.__username_field = page.locator("[data-test=\"username\"]").describe("Username Field")
        self.__password_field = page.locator("[data-test=\"password\"]").describe("Password Field")
        self.__login_button = page.locator("[data-test=\"login-button\"]").describe("Login Button")
        self.__error_message = page.locator("[data-test=\"error\"]").describe("Login Error Message")
        self.__login_credentials = page.locator("[data-test=\"login-credentials\"]").describe("Login Credentials Section")

# # Methods

    def click_login_button(self):
        with allure.step("Clicking 'Login' button"):
            self.__login_button.click()

    def fill_password(self, password: str):
        with allure.step(f"Typing '{password}' into password field"):
            self.__password_field.fill(password)

    def navigate(self, url = "https://www.saucedemo.com/"):
        with allure.step(f"Navigating to url: '{url}'"):
            self.__page.goto(url)

    def type_username(self, username: str):
        with allure.step(f"Typing '{username}' into username field"):
            self.__username_field.press_sequentially(username, delay=100)


# # Assertions

    def expect_error_message(self, expected_text: str):
        with allure.step(f"Expecting error message to contain: '{expected_text}'"):
            expect(self.__error_message).to_contain_text(expected_text)

    def expect_login_credentials_visible(self):
        with allure.step("Expecting login credentials section to be visible"):
            expect(self.__login_credentials).to_be_visible()