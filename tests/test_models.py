import unittest
import sqlite3
import os
from app.models import add_employee, get_employees, init_db

class TestModels(unittest.TestCase):
    DB_PATH = 'test_employee.db'

    def setUp(self):
        # Set up a temporary test database
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                position TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def tearDown(self):
        # Remove the test database after the test is done
        if os.path.exists(self.DB_PATH):
            os.remove(self.DB_PATH)

    def test_add_employee(self):
        # Test if an employee is added to the database correctly
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        add_employee('Jane Doe', 25, 'Designer')
        cursor.execute('SELECT * FROM employees WHERE name=?', ('Jane Doe',))
        employee = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(employee)
        self.assertEqual(employee[1], 'Jane Doe')
        self.assertEqual(employee[2], 25)
        self.assertEqual(employee[3], 'Designer')

    def test_get_employees(self):
        # Test if the get_employees function retrieves employees from the database
        add_employee('John Smith', 28, 'Manager')
        employees = get_employees()

        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0][1], 'John Smith')
        self.assertEqual(employees[0][2], 28)
        self.assertEqual(employees[0][3], 'Manager')

if __name__ == '__main__':
    unittest.main()
