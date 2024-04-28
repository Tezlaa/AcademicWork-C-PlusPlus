from models.employees.employee import Employee
from models.patient import Patient


class Database:
    hash_database = {}
    employees: list[Employee] = []
    patients: list[Patient] = []
    
    def __init__(self, db) -> None:
        self.db = db
        
    def add_employee(self, employee: Employee) -> None:
        employee_key = employee.employee_key
        if employee_key in self.hash_database:
            return
        self.hash_database[employee_key] = employee
        self.employees.append(employee)
    
    def delete_employee(self, employee: Employee) -> None:
        employee_key = employee.employee_key
        if employee_key not in self.hash_database:
            return
        del self.hash_database[employee_key]
        self.employees.remove(employee)
    
    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)