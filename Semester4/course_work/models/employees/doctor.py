from datetime import datetime

from typing import Optional

from models.employees.intern import Intern
from models.patient import Patient


class Doctor(Intern):
    def __init__(self, first_name: str,
                 second_name: str,
                 age: int,
                 password: str,
                 salary: Optional[float] = None) -> None:
        super().__init__(first_name, second_name, age, password, salary)

    def method_set_patient_diagnosis(self, patient: Patient, diagnosis: str) -> None:
        patient.diagnosis = diagnosis

    def method_checkout_patient(self, patient: Patient, checkout_date: datetime | None) -> None:
        if not checkout_date:
            checkout_date = datetime.now()
        patient.checkout_date = checkout_date
