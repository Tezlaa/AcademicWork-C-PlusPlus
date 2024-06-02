from typing import Optional

from common.tools import Tools
from models.person import Person


class Employee(Person):
    def __init__(self, first_name: str,
                 second_name: str,
                 age: int,
                 password: str,
                 salary: Optional[float] = None) -> None:
        self._minimal_age = 18
        self._maximal_age = 55
        super().__init__(first_name, second_name, age)

        self._login = self.second_name
        self._password = password
        self._salary = salary

    def _is_admin(self) -> bool:
        return False

    def _is_owner(self, login: str, password: str) -> bool:
        return self._login == login and self._password == password

    def __get_employee_key(self) -> str:
        return Tools.generate_secret_key(self._login, self._password)

    def __str__(self) -> str:
        return f'{super().__str__()}\n\nPosition: {self.__class__.__name__}'

    salary = property(lambda self: self._salary)
    employee_key = property(__get_employee_key)
