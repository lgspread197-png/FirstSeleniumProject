from selenium.webdriver.common.by import By


class TestLocators:
    def test_locators_strategies(self, main_page):
        # NAME: except for meta tags, there are only six elements with attribute 'name' on the main page
        email_input = main_page.find_element(By.NAME, "NewsletterEmail")
        email_input = main_page.find_element(By.ХPATH, "NewsletterEmail")
        search_input = main_page.find_element(By.NAME, "q")
        poll_answers = main_page.find_elements(By.NAME, "pollanswers-1")
        assert len(poll_answers) == 4