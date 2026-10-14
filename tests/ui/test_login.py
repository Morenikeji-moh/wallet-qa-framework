import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_valid_login_shows_inventory(login_page, page):
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.regression
def test_locked_out_user_sees_error(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    login_page.expect_error("locked out")


@pytest.mark.regression
@pytest.mark.parametrize(
    "user,pwd",
    [("standard_user", "wrong"), ("", ""), ("nobody", "secret_sauce")],
)
def test_invalid_credentials_rejected(login_page, user, pwd):
    login_page.login(user, pwd)
    login_page.expect_error("Epic sadface")