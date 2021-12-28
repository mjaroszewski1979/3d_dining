from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    


class HomePage(BasePage):

    def is_title_matches(self):
        return "3 Dining | Home" in self.driver.title

    def is_form_link_works(self):
        self.do_click(HomePageLocators.FORM_LINK)
        return "3 Dining | Book" in self.driver.title

    def is_home_link_works(self):
        self.do_click(HomePageLocators.NEON_BUTTON)
        return "3 Dining | Home" in self.driver.title

    def is_menu_link_works(self):
        self.do_click(HomePageLocators.MENU_LINK)
        return "3 Dining | Menu" in self.driver.title




   