import sqlite3

from typing import Optional

from base.repository import Repository

from common.exceptions import LoginFailed
from common.tools import Tools

from models.employees.employee import Employee
from models.patient import Patient


class HospitalAccount:
    def __init__(self) -> None:
        self.account: Optional[Employee] = None
        self.repository = Repository(sqlite3.connect('database.db'))
    
    def login(self, login: str, password: str) -> None:
        secret_key = Tools.generate_secret_key(login, password)
        account = self.repository.hash_database.get(secret_key)
        if not account:
            raise LoginFailed('Login or password is incorrect')
        self.account = account
    
    def available_methods(self) -> list[str]:
        all_methods = dir(self.account)
        result = list(filter(lambda x: x.startswith('method_'), all_methods))
        return result
    
    def employees(self) -> list[Employee]:
        return self.repository.employees
    
    def patients(self) -> list[Patient]:
        return self.repository.patients