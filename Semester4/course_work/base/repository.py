import sqlite3

from base.database import DatabaseManager

from models.employees.employee import Employee
from models.patient import Patient
from models import employees as emp

from common.tools import Tools


class Repository(DatabaseManager):
    hash_database = {}
    employees: list[Employee] = []
    patients: list[Patient] = []

    def __init__(self, db_connection: sqlite3.Connection) -> None:
        super().__init__(db_connection)
        self.__download_employess()
        self.__download_patients()

    def __download_employess(self) -> None:
        for position, f_name, s_name, age, password, salary in self._get_employees():
            self.add_employee(
                emp.__dict__.get(position, emp.Employee)(f_name, s_name, age, password, salary)
            )

    def __download_patients(self) -> None:
        for (f_name, s_name, age, profession,
             address, profession_diseases, diagnosis,
             entry_date, checkout_date) in self._get_patients():
            self.add_patient(
                Patient(
                    f_name, s_name, age, profession,
                    address, profession_diseases, diagnosis,
                    Tools.string_to_datetime(entry_date),
                    Tools.string_to_datetime(checkout_date),
                )
            )

    def __load_employess(self) -> None:
        for employee in self.employees:
            self._set_employee(employee)

    def __load_patients(self) -> None:
        for patient in self.patients:
            self._set_patient(patient)

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

    def __del__(self) -> None:
        self._claer_tables()
        self.__load_employess()
        self.__load_patients()
