from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_example_1(login_page) -> None:
    login_page.navigate()
    login_page.expect_login_credentials_visible()

    login_page.type_username("locked_out_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()

    login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")


def test_example_2(page: Page, login_page) -> None:
    login_page.navigate()
    login_page.expect_login_credentials_visible()

    login_page.type_username("abcabc")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_error_message("Epic sadface: Username and password do not match any user in this service")


#לסדר את כל ההמשך כמו הפונקצית בדיקה למעלה...

def test_example_3(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"login-credentials\"]")).to_be_visible()

    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")

def test_example_4(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"login-credentials\"]")).to_be_visible()

    page.locator("[data-test=\"username\"]").press_sequentially("abcabc", delay=100)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Password is required")
