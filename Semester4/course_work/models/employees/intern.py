from datetime import datetime

from typing import Any, Optional

from models.employees.employee import Employee
from models.patient import Patient


class Intern(Employee):
    def __init__(self, first_name: str,
                 second_name: str,
                 age: int,
                 password: str,
                 salary: Optional[float] = None) -> None:
        super().__init__(first_name, second_name, age, password, salary)

    def method_register_parient(self, first_name: str,
                                second_name: str, age: int,
                                profession: str,
                                address: str,
                                profession_diseases: Optional[str] = None,
                                entry_date: Optional[datetime] = None) -> Patient:
        return Patient(
            first_name=first_name,
            second_name=second_name,
            age=age,
            profession=profession,
            address=address,
            profession_diseases=profession_diseases,
            entry_date=entry_date,
        )
    
    def method_change_patient(self, patient: Patient, field: str, value: Any) -> None:
        patient.__setattr__(field, value)