from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class Page(object):
    def __init__(self, driver, base_url='http://yahoo.co.jp/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_titile(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url()

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def check_element_exists(self, *locator):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def checkbox_is_selected(self, *locator):
        return True if (self.find_element(*locator).is_selected()) else False

    def wait_for_element(self, *locator):
        return WebDriverWait(self.driver, 30).until(lambda self: self.find_element(*locator))