import os

from base.hospital import HospitalAccount

from common.exceptions import LoginFailed
from common.tools import Tools


class ConsoleCommands:
    def show_list(self, _list: list) -> None:
        os.system('cls')
        for i, item in enumerate(_list):
            print(self.select_by_lines(f'#{i} - {item}'))

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
            elif option == '02':
                self.list_to_last_message(self.hospital.patients())
            
            if int(option) not in self.methods:
                continue
            
            if self.methods[int(option)][0] in self.__dir__():
                self.__getattribute__(self.methods[int(option)][0])()
    
    def login(self):
        print('Enter login and password:')
        try:
            self.hospital.login('admin', 'admin')
            # self.hospital.login(self.cursor_waiter('login'), self.cursor_waiter('password'))
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
        self.show_list(patients)
        
        patient_number = int(self.cursor_waiter('select patient number'))
        if not 0 <= patient_number < len(patients):
            return
        
        patient = patients[patient_number]
        diagnosis = self.cursor_waiter('diagnosis')
        self.hospital.account.method_set_patient_diagnosis(patient, diagnosis)  # type: ignore
    
    def checkout_patient(self) -> None:
        patients = self.hospital.patients()
        self.show_list(patients)
        
        patient_number = int(self.cursor_waiter('select patient number'))
        if not 0 <= patient_number < len(patients):
            return
        
        patient = patients[patient_number]
        checkout_date_str = self.cursor_waiter('checkout date in format YYYY-MM-DD HH:MM:SS')
        checkout_date = Tools.string_to_datetime(checkout_date_str)
        self.hospital.account.method_checkout_patient(patient, checkout_date)  # type: ignore
    
    def set_salary(self) -> None:
        employee = self.hospital.employees()
        self.show_list(employee)
        
        employee_number = int(self.cursor_waiter('select employee number'))
        if not 0 <= employee_number < len(employee):
            return
        
        employee = employee[employee_number]
        salary = float(self.cursor_waiter('new salary'))
        self.hospital.account.method_set_salary(employee, salary)  # type: ignore
        