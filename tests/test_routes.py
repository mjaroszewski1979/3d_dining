import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))  
parent = os.path.dirname(current)  
sys.path.append(parent)

import run


app = run.create_app()


class RoutesTestCase(unittest.TestCase):


    # Ensures that the application instance exists
    def test_app_exists(self):
        self.assertIsNotNone(app)

    # Ensures that index page loads correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the index page
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'3 Dining' in response.data)

    # Ensures that menu page loads correctly
    def test_menu(self):
        tester = app.test_client(self)
        response = tester.get('/menu', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the menu page
    def test_menu_data(self):
        tester = app.test_client(self)
        response = tester.get('/menu', content_type='html/text')
        self.assertTrue(b'3 Course Set' in response.data)

    # Ensures that form page loads correctly
    def test_form(self):
        tester = app.test_client(self)
        response = tester.get('/form', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the form page
    def test_form_data(self):
        tester = app.test_client(self)
        response = tester.get('/form', content_type='html/text')
        self.assertTrue(b'Booking Date' in response.data)

    # Ensures that form accepts only correct input
    def test_form_post_too_many_guests(self):
        tester = app.test_client(self)
        response = tester.post('/form', 
        data=dict(book_date='30.08.2021', guests=36, email='john@gmail.com',  follow_redirects=True))
        self.assertIn(b'Sorry, maximum number of guests per day is 30.', response.data)

    # Ensures that form works correctly given valid date, guests number and email
    def test_form_post_weekend(self):
        tester = app.test_client(self)
        response = tester.post('/success', 
        data=dict(book_date = '03.09.2021', guests='4', email='mjaro@gmail.com'))
        self.assertIn(b'Thank You for Your Reservation!', response.data)

    # Ensures that admin page loads correctly
    def test_admin(self):
        tester = app.test_client(self)
        response = tester.get('/admin', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the admin page
    def test_admin_data(self):
        tester = app.test_client(self)
        response = tester.get('/admin', content_type='html/text')
        self.assertTrue(b'Enter Booking Date' in response.data)

    # Ensures that result page loads correctly
    def test_result_post_status(self):
        tester = app.test_client(self)
        response = tester.post('/result', 
        data=dict(date='31.08.2021',  follow_redirects=True))
        self.assertEqual(response.status_code, 200)

    # Ensures that result page loads correctly given invalid date
    def test_result_post(self):
        tester = app.test_client(self)
        response = tester.post('/result', 
        data=dict(date='Tue, 3 Aug 2021 00:00:00 GMT',  follow_redirects=True))
        self.assertIn(b'There are no bookings on the date you have selected!', response.data)

    # Ensures that error/404 page loads correctly
    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # Ensures that the data returned contains actual text from the error/404 page
    def test_404_data(self):
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertTrue(b'the website you were looking for' in response.data)



if __name__ == '__main__':
    unittest.main()