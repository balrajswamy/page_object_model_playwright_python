

class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigate_url(self):

        self.page.goto("https://app.vwo.com", wait_until="load")

    @property
    def username_field(self):
        return self.page.wait_for_selector("//input[@id='login-username']")

    @property
    def password_field(self):
        return self.page.wait_for_selector("//input[@id='login-password']")

    @property
    def submit_button(self):
        return self.page.wait_for_selector("//button[@id='js-login-btn']")

    def submit_login_form(self,user):

        self.username_field.fill(user["username"])
        self.password_field.fill(user["password"])
        self.submit_button.click()


