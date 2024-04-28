import sqlite3

from models.patient import Patient
from models.employees.employee import Employee

from common.tools import Tools


class DatabaseManager:
    def __init__(self, db_connection: sqlite3.Connection) -> None:
        self.__cur = db_connection.cursor()
        self.__connect = db_connection
        self.__table_patients()
        self.__table_employees()
    
    def __sql_query_and_commit(self, sql: str) -> None:
        self.__cur.execute(sql)
        self.__connect.commit()
        
    def __table_patients(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS patients(
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                second_name TEXT NOT NULL,
                age INTEGER NOT NULL,
                profession TEXT NOT NULL,
                address TEXT NOT NULL,
                profession_diseases TEXT NOT NULL,
                diagnosis TEXT DEFAULT NULL,
                entry_date TEXT DEFAULT NULL,
                checkout_date TEXT DEFAULT NULL
            )
        """
        self.__sql_query_and_commit(sql)

    def __table_employees(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY,
                position_name TEXT NOT NULL,
                first_name TEXT NOT NULL,
                second_name TEXT NOT NULL,
                age INTEGER NOT NULL,
                password TEXT NOT NULL,
                salary REAL DEFAULT NULL
            )
        """
        self.__sql_query_and_commit(sql)
    
    def _get_patients(self) -> list[tuple]:
        sql = """
            SELECT
                first_name, second_name, age, profession,
                address, profession_diseases, diagnosis, entry_date,
                checkout_date
            FROM patients
        """
        return self.__cur.execute(sql).fetchall()
    
    def _get_employees(self) -> list[tuple]:
        sql = """
            SELECT
                position_name, first_name,
                second_name, age, password, salary
            FROM employees
        """
        return self.__cur.execute(sql).fetchall()
    
    def _claer_tables(self) -> None:
        for table in ['employees', 'patients']:
            sql = f"DELETE FROM {table}"
            self.__sql_query_and_commit(sql)
    
    def _set_employee(self, employee: Employee) -> None:
        sql = """
            INSERT INTO employees(position_name, first_name, second_name, age, password, salary)
            VALUES(?, ?, ?, ?, ?, ?)
        """
        self.__cur.execute(sql, (employee.__class__.__name__,
                                 employee.first_name,
                                 employee.second_name,
                                 employee.age,
                                 employee._password,
                                 employee.salary))
        self.__connect.commit()
        
    def _set_patient(self, patient: Patient) -> None:
        sql = """
            INSERT INTO patients(
                first_name, second_name, age, profession, address,
                profession_diseases, diagnosis, entry_date, checkout_date
            ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.__cur.execute(sql, (patient.first_name,
                                 patient.second_name,
                                 patient.age,
                                 patient.profession,
                                 patient.address,
                                 patient.profession_diseases,
                                 patient.diagnosis,
                                 Tools.datetime_to_string(patient.entry_date),
                                 Tools.datetime_to_string(patient.checkout_date)))
        self.__connect.commit()