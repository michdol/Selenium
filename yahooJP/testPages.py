import unittest
from yahooJP.pages import *
from selenium import webdriver

class TestPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://yahoo.co.jp')

    def test_check_page_loaded(self):
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_login_to_email(self):
        page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        mail_page = MailPage(self.driver)
        page.go_to_mail_page()
        self.assertTrue(login_page.check_page_loaded())
        login_page.login('Michal')
        self.assertTrue(mail_page.check_page_loaded())

    def test_get_emails_and_log_out(self):
        page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        mail_page = MailPage(self.driver)
        page.go_to_mail_page()
        login_page.login('Michal')
        emails = mail_page.get_emails()
        print(emails)
        self.assertTrue(mail_page.log_out())

    def test_login_invalid_user(self):
        page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        page.go_to_mail_page()
        self.assertTrue(login_page.login_invalid_user('Invalid'))

    def test_search(self):
        page = MainPage(self.driver)
        search_result_page = SearchResultPage(self.driver)
        self.assertTrue(page.enter_search_term('selenium webdriver creator'))
        search_result_page.go_to_result()
        search_result_page.get_contributors_names()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()