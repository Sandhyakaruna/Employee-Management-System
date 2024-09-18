import unittest
from app import create_app
from flask import url_for

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # Set up the test app and test client
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_index_page(self):
        # Test if the index page loads correctly
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Employee Management System", response.data)

    def test_view_employees_page(self):
        # Test if the employees page loads correctly
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee List", response.data)

    def test_add_employee_page(self):
        # Test if the add employee page loads correctly (GET request)
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Add Employee", response.data)

    def test_add_employee_post(self):
        # Test the POST request to add an employee
        response = self.client.post('/add', data=dict(
            name='John Doe',
            age=30,
            position='Developer'
        ), follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"John Doe", response.data)

if __name__ == '__main__':
    unittest.main()
