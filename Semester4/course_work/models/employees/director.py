from typing import Any, Optional

from models.employees.doctor import Doctor
from models.employees.employee import Employee
from models.employees.intern import Intern


class Director(Doctor, Intern):
    def __init__(self, first_name: str,
                 second_name: str,
                 age: int,
                 password: str,
                 salary: Optional[float] = None) -> None:
        super().__init__(first_name, second_name, age, password, salary)
    
    def _is_admin(self) -> bool:
        return True

    def method_set_salary(self, employee: Employee, value: float) -> None:
        employee._salary = value
    
    def method_register_employee(self, position: str,
                                 f_name: str,
                                 s_name: str,
                                 age: int,
                                 password: str,
                                 salary: float) -> Employee:
        positions = {'Director': self, 'Doctor': Doctor, 'Intern': Intern}
        return positions.get(position, Employee)(f_name, s_name, age, password, salary)

    def method_change_employee(self, patient: Employee, field: str, value: Any) -> None:
        patient.__setattr__(field, value)