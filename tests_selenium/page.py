from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from locators import BookPageLocators, ErrorPageLocators, HomePageLocators, MenuPageLocators
from selenium.webdriver.common.action_chains import ActionChains




class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

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

class MenuPage(BasePage):

    def is_title_matches(self):
        return "3 Dining | Menu" in self.driver.title

    def is_info_displayed_correctly(self):
        info_text = self.get_element_text(MenuPageLocators.INFO)
        return 'Info' in info_text

    def is_manage_booking_button_works(self):
        action = ActionChains(self.driver)
        front = self.get_elements(MenuPageLocators.FRONT)
        action.move_to_element(front[1]).perform()
        self.do_click(MenuPageLocators.MANAGE_BUTTON)
        return "3 Dining | Book" in self.driver.title

class BookPage(BasePage):

    def is_title_matches(self):
        return "3 Dining | Book" in self.driver.title

    def is_form_works_given_valid_data(self):
        self.do_send_keys(BookPageLocators.DATE, '11/10/2022')
        self.do_send_keys(BookPageLocators.GUESTS, 2)
        self.do_send_keys(BookPageLocators.EMAIL, 'mj@gmail.com')
        self.do_click(BookPageLocators.SUBMIT)
        return "3 Dining | Success" in self.driver.title

    def is_form_works_given_invalid_number_of_guests(self):
        self.do_send_keys(BookPageLocators.DATE, '11/10/2022')
        self.do_send_keys(BookPageLocators.GUESTS, 222)
        self.do_send_keys(BookPageLocators.EMAIL, 'mj@gmail.com')
        self.do_click(BookPageLocators.SUBMIT)
        error_msg = self.get_element_text(BookPageLocators.ERROR_MSG)
        return "Sorry, maximum number of guests per day is 30." in error_msg

    def is_form_works_given_invalid_date(self):
        self.do_clear(BookPageLocators.DATE)
        self.do_clear(BookPageLocators.GUESTS)
        self.do_clear(BookPageLocators.EMAIL)
        self.do_send_keys(BookPageLocators.DATE, '20/11/2022')
        self.do_send_keys(BookPageLocators.GUESTS, 2)
        self.do_send_keys(BookPageLocators.EMAIL, 'mj@gmail.com')
        self.do_click(BookPageLocators.SUBMIT)
        error_msg = self.get_element_text(BookPageLocators.ERROR_MSG)
        return "Sorry, we are closed on weekends. Please choose a different date." in error_msg


class ErrorPage(BasePage):

    def is_title_matches(self):
        return "3 Dining | 404" in self.driver.title

    def is_error_msg_displayed(self):
        error_msg_text = self.get_element_text(ErrorPageLocators.ERROR_MSG)
        return "Sorry, we can’t find the website you were looking for." in error_msg_text




   
   
