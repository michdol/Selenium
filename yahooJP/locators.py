from selenium.webdriver.common.by import By


class MainPageLocators(object):
    HEADER              = (By.XPATH, "//*[@id='masthead']/h1/a/img")
    SEARCHBAR           = (By.ID, "srchtxt")
    SEARCHBUTTON        = (By.ID, "srchbtn")
    MAIL    = (By.XPATH, "//*[@id='mhi6th']/a")


class LoginPageLocators(object):
    HEADER              = (By.ID, "ygmhlog")
    EMAIL               = (By.ID, "username")
    PASSWORD            = (By.ID, "passwd")
    LOGINBUTTON         = (By.ID, ".save")
    FAILEDLOGIN         = (By.XPATH, ".//*[@id='themeBox']/div[1]/h2")


class MailPageLocators(object):
    HEADER              = (By.ID, "ygmhlog")
    LOGOUT              = (By.XPATH, "//*[@id='normalHeader']/div[2]/a[3]")
    CONFIRMLOGOUT       = (By.XPATH, "//*[@id='yregct']/div[1]/h1")
    EMAILS              = (By.CLASS_NAME, "list-view-items-inner")
    THEEMAIL            = (By.XPATH, ".//div[@data-action='select-message']")
    SENDER              = (By.XPATH, ".//div[@class='from']")
    TITLE               = (By.XPATH, ".//div[@class='subj']")

class SearchResultsPageLocators(object):
    SEARCHBAR           = (By.ID, 'yschsp')
    CONTRIBUTORS        = (By.LINK_TEXT, 'Selenium Contributors')
    LIST                = (By.ID, 'mainContent')
    SELENIUMHEADER      = (By.XPATH, ".//*[@id='header']/h1/a")
    NAMES                = (By.XPATH, ".//div[@class='contributor']/h3/a")