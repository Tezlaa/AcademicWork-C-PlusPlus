from typing import Optional
from models.parson import Person


class Employee(Person):
    def __init__(self, first_name: str, second_name: str, age: int, password: str) -> None:
        super().__init__(first_name, second_name, age)
        self._login = self.second_name
        self._password = password
        self._salary = None
        self._minimal_age = 18
        self._maximal_age = 55

    def _is_admin(self) -> bool:
        return False
    
    def _is_owner(self, login: str, password: str) -> bool:
        return self._login == login and self._password == password
    
    def set_salary(self, employee: 'Employee', value: float) -> None:
        if not employee._is_admin():
            raise PermissionError('Only admin can change salary')
        self._salary = value
    
    def __get_eployee_key(self) -> str:
        return self._login + self._password
    
    def __str__(self) -> str:
        return f'{super().__str__()}\n\nPosition: {self.__class__.__name__}'
    
    salary = property(lambda self: self._salary)
    employee_key = property(__get_eployee_key)