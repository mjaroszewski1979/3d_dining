from flask import url_for
from selenium import webdriver
import page
from run import create_app
from extensions import db
import unittest
import time



class TestBase(unittest.TestCase):


    def setUp(self):
        app = create_app()
        app.app_context().push()
        self.driver =  webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_size(1920, 1080)
        db.session.commit()
        db.drop_all()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.driver.close()


class SeleniumTest(TestBase):
        
    def test_home_page(self):
        self.driver.get('http://127.0.0.1:5000/')
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_form_link_works()
        assert home_page.is_home_link_works()
        assert home_page.is_menu_link_works()

    def test_menu_page(self):
        self.driver.get('http://127.0.0.1:5000/menu')
        menu_page = page.MenuPage(self.driver)
        assert menu_page.is_title_matches()
        assert menu_page.is_info_displayed_correctly()
        assert menu_page.is_manage_booking_button_works()

    def test_error_page(self):
        self.driver.get('http://127.0.0.1:5000/error')
        error_page = page.ErrorPage(self.driver)
        assert error_page.is_title_matches()
        assert error_page.is_error_msg_displayed()

    def test_book_page(self):
        self.driver.get('http://127.0.0.1:5000/form')
        book_page = page.BookPage(self.driver)
        assert book_page.is_title_matches()
        assert book_page.is_form_works_given_invalid_number_of_guests()
        assert book_page.is_form_works_given_invalid_date()
        assert book_page.is_form_works_when_fully_booked()
        assert book_page.is_form_works_given_valid_data()



if __name__ == '__main__':
    unittest.main()
