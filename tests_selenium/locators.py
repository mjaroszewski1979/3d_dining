from selenium.webdriver.common.by import By

class HomePageLocators(object):

    FORM_LINK = (By.CLASS_NAME, 'form-link')
    NEON_BUTTON = (By.CLASS_NAME, 'neon-button')
    MENU_LINK = (By.CLASS_NAME, 'menu-link')

class MenuPageLocators(object):

    INFO = (By.CLASS_NAME, 'info')
    FRONT = (By.CLASS_NAME, 'front')
    MANAGE_BUTTON = (By.LINK_TEXT, 'Manage Your Booking')

class BookPageLocators(object):

    BOOK_DATE = (By.NAME, 'book_date')
    GUESTS = (By.NAME, 'guests')
    EMAIL = (By.NAME, 'email')
    SUBMIT_BOOK = (By.NAME, 'submit')
    ERROR_MSG = (By.ID, 'error_msg')
    ERROR = (By.CLASS_NAME, 'error')

class AdminPageLocators(object):

    DATE = (By.NAME, 'date')
    SUBMIT = (By.CLASS_NAME, 'submit')
    FORM_ERROR = (By.CLASS_NAME, 'form-error')
    EMAILS = (By.CLASS_NAME, 'emails')
    

class ErrorPageLocators(object):

    ERROR_MSG = (By.CLASS_NAME, 'error-msg')
    



