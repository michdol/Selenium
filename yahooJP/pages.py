from yahooJP.base import Page
from yahooJP.locators import *
from time import sleep
from yahooJP.users import get_password, get_email
from yahooJP.excel_users import excel_get_email, excel_get_password


class MainPage(Page):
    def check_page_loaded(self):
        return self.find_element(*MainPageLocators.HEADER)

    def go_to_mail_page(self):
        self.find_element(*MainPageLocators.MAIL).click()
        self.wait_for_element(*LoginPageLocators.HEADER)
        return LoginPage(self.driver)

    def enter_search_term(self, term):
        searchbar = self.find_element(*MainPageLocators.SEARCHBAR)
        searchbutton = self.find_element(*MainPageLocators.SEARCHBUTTON)
        searchbar.send_keys(term)
        sleep(1)
        searchbutton.click()
        results_search_bar = self.wait_for_element(*SearchResultsPageLocators.SEARCHBAR)
        return results_search_bar.get_attribute('value') == term


class SearchResultPage(Page):
    def go_to_result(self):
        self.find_element(*SearchResultsPageLocators.CONTRIBUTORS).click()
        self.wait_for_element(*SearchResultsPageLocators.SELENIUMHEADER)

    def get_contributors_names(self):
        list = self.find_element(*SearchResultsPageLocators.LIST)
        names = list.find_elements(*SearchResultsPageLocators.NAMES)
        for name in names:
            print(name.text)


class LoginPage(Page):
    def check_page_loaded(self):
        return self.find_element(*LoginPageLocators.HEADER)

    def enter_email(self, name):
        self.driver.find_element(*LoginPageLocators.EMAIL).send_keys(get_email(name))

    def enter_password(self, name):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(get_password(name))

    def click_login(self):
        self.driver.find_element(*LoginPageLocators.LOGINBUTTON).click()

    def login(self, name):
        self.enter_email(name)
        self.enter_password(name)
        sleep(1)
        self.click_login()
        self.wait_for_element(*MailPageLocators.HEADER)
        return MailPage(self.driver)

    def login_invalid_user(self, name):
        self.enter_email(name)
        self.enter_password(name)
        sleep(1)
        self.click_login()
        return self.check_element_exists(*LoginPageLocators.FAILEDLOGIN)

    # Same methods for login as above but using excel for storing data

    def excel_enter_email(self, name):
        self.driver.find_element(*LoginPageLocators.EMAIL).send_keys(excel_get_email(name))

    def excel_enter_password(self, name):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(excel_get_password(name))

    def excel_login(self, name):
        self.excel_enter_email(name)
        self.excel_enter_password(name)
        sleep(1)
        self.click_login()
        self.wait_for_element(*MailPageLocators.HEADER)
        return MailPage(self.driver)

    def excel_login_invalud_user(self, name):
        self.excel_enter_email(name)
        self.excel_enter_password(name)
        sleep(1)
        self.click_login()
        return self.check_element_exists(*LoginPageLocators.FAILEDLOGIN)


class MailPage(Page):
    def check_page_loaded(self):
        return self.find_element(*MailPageLocators.HEADER)

    def log_out(self):
        self.find_element(*MailPageLocators.LOGOUT).click()
        return self.wait_for_element(*MailPageLocators.CONFIRMLOGOUT)

    def get_emails(self):
        emails_list = self.find_element(*MailPageLocators.EMAILS)
        emails = emails_list.find_elements(*MailPageLocators.THEEMAIL)
        emails_to_return = []
        for index, i in enumerate(emails):
            sender = i.find_element(*MailPageLocators.SENDER).text
            title = i.find_element(*MailPageLocators.TITLE).text
            emails_to_return.append({'index':index + 1, 'sender': sender, 'title': title})

        return emails_to_return
