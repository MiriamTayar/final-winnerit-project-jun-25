from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("2")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("abc")
    page.locator("[data-test=\"lastName\"]").fill("def")
    page.locator("[data-test=\"postalCode\"]").fill("058")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"pony-express\"]")).to_be_visible()
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test=\"back-to-products\"]")).to_be_visible()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
