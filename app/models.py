import sqlite3

DB_PATH = 'database/employee.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
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

def add_employee(name, age, position):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, age, position) VALUES (?, ?, ?)', (name, age, position))
    conn.commit()
    conn.close()

def get_employees():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return employees
