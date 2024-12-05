

class Dashboard:

    def __init__(self, page):
        self.page = page

    def get_logged_in_username(self):
        self.page.wait_for_load_state("networkidle")
        return self.page.locator("//h1[@data-qa='page-heading']").inner_text(timeout=5000)