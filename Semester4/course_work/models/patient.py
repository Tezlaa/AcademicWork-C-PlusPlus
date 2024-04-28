
from datetime import datetime
from typing import Optional
from models.parson import Person


class Patient(Person):
    def __init__(self, first_name: str,
                 second_name: str,
                 age: int,
                 profession: str,
                 address: str,
                 profession_diseases: str,
                 diagnosis: Optional[str],
                 entry_date: Optional[datetime],
                 checkout_date: Optional[datetime]) -> None:
        super().__init__(first_name, second_name, age)
        self.profession = profession
        self.profession_diseases = profession_diseases
        self.address = address
        self.diagnosis = diagnosis
        self.entry_date = entry_date
        self.checkout_date = checkout_date
    
    def __str__(self) -> str:
        return (f'{super().__str__()}\n\n'
                f'Profession: {self.profession}\n'
                f'Profession diseases: {self.profession_diseases}\n'
                f'Address: {self.address}\n'
                f'Diagnosis: {self.diagnosis}\n'
                f'Entry date: {self.entry_date}\n'
                f'Checkout date: {self.checkout_date}')