
import pytest
import allure
from tests.ex_05122024.POM.Pages.login_page import LoginPage
from tests.ex_05122024.POM.Pages.dashboad_page import Dashboard

user = {"username": "xxxx@gmail.com",
        "password": "yyyy"}

class TestLogin:

    @allure.title("TestCase#1 - to test login at https://app.vwo.com")
    def test_valid_login(self,page):

        login_page = LoginPage(page)
        dashboard_page = Dashboard(page)

        login_page.navigate_url()
        login_page.submit_login_form(user)

        username_text  = dashboard_page.get_logged_in_username()

        assert username_text == "Dashboard", "it is not login success!"




