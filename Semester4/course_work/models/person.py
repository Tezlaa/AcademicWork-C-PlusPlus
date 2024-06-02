from typing import Optional


class Person:
    _first_name: str
    _second_name: str
    _age: int
    _minimal_age = 5
    _maximal_age = 101

    def __init__(self, first_name: str, second_name: str, age: int) -> None:
        self._set_first_name(first_name)
        self._set_second_name(second_name)
        self._set_age(age)

    def _set_first_name(self, value: str) -> None:
        self._valid_name(value)
        self._first_name = value

    def _get_first_name(self) -> str:
        return self._first_name

    def _set_second_name(self, value: str) -> None:
        self._valid_name(value)
        self._second_name = value

    def _get_second_name(self) -> str:
        return self._second_name

    def _set_age(self, value: int) -> None:
        self._valid_age(value)
        self._age = value

    def _get_age(self) -> int:
        return self._age

    def _valid_name(self, value: str) -> Optional[Exception]:
        if len(value) <= 1 and value[0] != value[0].upper():
            raise ValueError(f'Unvalid value: {value}')

    def _valid_age(self, age: int) -> Optional[Exception]:
        if self._minimal_age >= age <= self._maximal_age:
            raise ValueError('Unvalid age. '
                             f'{self._minimal_age} >= {age} <= {self._maximal_age}')

    def __str__(self) -> str:
        return (f'First name: {self._first_name}\n'
                f'Second name: {self._second_name}\n'
                f'Age: {self._age}')

    first_name = property(_get_first_name, _set_first_name)
    second_name = property(_get_second_name, _set_second_name)
    age = property(_get_age, _set_age)
