import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


# מחליף את ברירת המחדל של הדפדפן כדי שיהיה headless=False
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict) -> dict:
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def login_page_with_login(page: Page):
    lp = LoginPage(page)
    lp.navigate()
    return lp