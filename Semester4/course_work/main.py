

from models.employees.employee import Employee


if __name__ == '__main__':
    p = Employee('John', 'Doe', 30, 'password')
    print(p.salary)