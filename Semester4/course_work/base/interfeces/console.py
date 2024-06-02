import os

from base.hospital import HospitalAccount

from common.exceptions import LoginFailed
from common.tools import Tools
from models.person import Person


class ConsoleCommands:
    def add_list_to_last_message(self, _list: list) -> None:
        message = ''
        for i, item in enumerate(_list):
            message += (self.select_by_lines(f'#{i} - {item}'))
        self.last_message = message

    def list_to_last_message(self, _list: list) -> None:
        self.last_message = ''
        for i, item in enumerate(_list):
            self.last_message += self.select_by_lines(f'#{i} - {item}')

    def show_methods(self, methods: dict[int, tuple[str, str]]) -> None:
        for i, method in methods.items():
            print(f'{i} - {method[1]}')

    def show_last_message(self) -> None:
        if self.last_message:
            print(self.last_message)
            self.last_message = None

    @staticmethod
    def cursor_waiter(message: str = '') -> str:
        return input(f'{message} >>> ')

    @staticmethod
    def select_by_lines(message: str) -> str:
        return f'\n{"_" * 15}\n{message}\n{"-" * 15}\n'


class Console(ConsoleCommands):
    def __init__(self) -> None:
        self.hospital = HospitalAccount()
        self.methods: dict[int, tuple[str, str]] = {}
        self.last_message = None

    def menu(self):
        while True:
            if not self.hospital.account:
                self.login()
                continue

            os.system('cls')
            self.show_last_message()
            print(f'{self.select_by_lines('Menu:')}')
            self.show_methods(self.methods)
            print('\n\n01 - Show employees\n02 - Show patients\n00 - Exit\n\n')

            option = self.cursor_waiter('option')
            if option == '00':
                break
            elif option == '01':
                self.list_to_last_message(self.hospital.employees())
                continue
            elif option == '02':
                self.list_to_last_message(self.hospital.patients())
                continue

            if int(option) not in self.methods:
                continue

            if self.methods[int(option)][0] in self.__dir__():
                self.__getattribute__(self.methods[int(option)][0])()

    def login(self):
        print('Enter login and password:')
        try:
            # self.hospital.login('admin', 'admin')  # for tests
            self.hospital.login(self.cursor_waiter('login'), self.cursor_waiter('password'))
        except LoginFailed:
            print('Login or password is incorrect')
            return
        self.methods = {
            i: (method.split('method_')[1], ' '.join(method.split('method_')[1].split('_')).capitalize())
            for i, method in enumerate(self.hospital.available_methods())
        }
        os.system('cls')

    def set_patient_diagnosis(self) -> None:
        patients = self.hospital.patients()
        self.add_list_to_last_message(patients)

        patient_number = int(self.cursor_waiter('select patient number'))
        if not 0 <= patient_number < len(patients):
            return

        patient = patients[patient_number]
        diagnosis = self.cursor_waiter('diagnosis')
        self.hospital.account.method_set_patient_diagnosis(patient, diagnosis)  # type: ignore

    def checkout_patient(self) -> None:
        patients = self.hospital.patients()
        self.add_list_to_last_message(patients)

        patient_number = int(self.cursor_waiter('select patient number'))
        if not 0 <= patient_number < len(patients):
            return

        patient = patients[patient_number]
        checkout_date_str = self.cursor_waiter('checkout date in format YYYY-MM-DD HH:MM:SS')
        checkout_date = Tools.string_to_datetime(checkout_date_str)
        self.hospital.account.method_checkout_patient(patient, checkout_date)  # type: ignore

    def set_salary(self) -> None:
        employee = self.hospital.employees()
        self.add_list_to_last_message(employee)

        employee_number = int(self.cursor_waiter('select employee number'))
        if not 0 <= employee_number < len(employee):
            return

        employee = employee[employee_number]
        salary = float(self.cursor_waiter('new salary'))
        self.hospital.account.method_set_salary(employee, salary)  # type: ignore

    def change_person(self, obj_person: Person) -> None:
        employee = self.hospital.employees()
        self.add_list_to_last_message(employee)
        self.show_last_message()

        employee_number = int(self.cursor_waiter('select employee number'))
        if not 0 <= employee_number < len(employee):
            return

        employee = employee[employee_number]
        params = [name for name in employee.__dir__() if not name.startswith(('__', '_', 'method_', 'employee_key'))]
        self.add_list_to_last_message(params)
        self.show_last_message()
        param_number = int(self.cursor_waiter('select param number'))
        if not 0 <= param_number < len(params):
            return

        param = params[param_number]
        new_value = self.cursor_waiter(f'new {param}')
        new_value = int(new_value) if new_value.isdigit() else new_value
        try:
            self.hospital.account.method_change_employee(employee, param, new_value)  # type: ignore
        except Exception as e:
            self.last_message = e

    def change_employee(self) -> None:
        employee = self.hospital.employees()
        if not employee:
            return
        self.add_list_to_last_message(employee)
        self.show_last_message()

        employee_number = int(self.cursor_waiter('select employee number'))
        if not 0 <= employee_number < len(employee):
            return

        employee = employee[employee_number]
        self.change_person(employee)

    def change_patient(self) -> None:
        patients = self.hospital.patients()
        if not patients:
            return
        self.add_list_to_last_message(patients)
        self.show_last_message()

        patient_number = int(self.cursor_waiter('select patient number'))
        if not 0 <= patient_number < len(patients):
            return

        patient = patients[patient_number]
        self.change_person(patient)

    def register_employee(self) -> None:
        position = self.cursor_waiter('Position (Doctor, Intern, Director): ')
        f_name = self.cursor_waiter('First name')
        s_name = self.cursor_waiter('Second name')
        age = int(self.cursor_waiter('Age'))
        password = self.cursor_waiter('Password')
        salary = float(self.cursor_waiter('Salary'))
        try:
            self.hospital.repository.employees.append(self.hospital.account.method_register_employee(    # type: ignore
                position, f_name, s_name, age, password, salary
            ))
        except Exception as e:
            self.last_message = e
            return

        self.last_message = f'Employee {position} {f_name} {s_name} was registered!'
        self.hospital.repository.__del__()

    def register_patient(self) -> None:
        first_name = self.cursor_waiter('First name')
        second_name = self.cursor_waiter('Second name')
        age = int(self.cursor_waiter('Age'))
        profession = self.cursor_waiter('Profession')
        address = self.cursor_waiter('Address')
        profession_diseases = self.cursor_waiter('Profession diseases')
        entry_date_str = self.cursor_waiter('Entry date in format YYYY-MM-DD HH:MM:SS')
        entry_date = Tools.string_to_datetime(entry_date_str)
        try:
            self.hospital.repository.patients.append(self.hospital.account.method_register_patient(  # type: ignore
                first_name, second_name, age, profession, address, profession_diseases, entry_date
            ))
        except Exception as e:
            self.last_message = e
            return

        self.last_message = f'Patient {first_name} {second_name} was registered!'
        self.hospital.repository.__del__()
