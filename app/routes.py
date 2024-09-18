from flask import Blueprint, render_template, request, redirect, url_for
from app.models import add_employee, get_employees

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/employees')
def view_employees():
    employees = get_employees()
    return render_template('view_employees.html', employees=employees)

@main_routes.route('/add', methods=['GET', 'POST'])
def add_employee_view():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        position = request.form.get('position')
        add_employee(name, age, position)
        return redirect(url_for('main_routes.view_employees'))
    return render_template('add_employee.html')
