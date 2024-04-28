from models.employees.employee import Employee


class Director(Employee):
    def __init__(self, first_name: str, second_name: str, age: int, password: str) -> None:
        super().__init__(first_name, second_name, age, password)
    
    def _is_admin(self) -> bool:
        return True