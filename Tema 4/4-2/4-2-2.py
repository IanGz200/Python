from datetime import datetime,date
from abc import abstractmethod, ABC

from gi.overrides import override
from icu import DateInterval


class Teacher(ABC):
    name:str
    surname:str
    address:str
    base_salary:float
    salary:float

    def teach(self)->None:
        print("Dou unha clase de programación en Python")

    @abstractmethod
    def generate_payroll(self)->None:
        pass

class CareerOfficer(Teacher):
    officer_complement:float
    opposition_Year:int
    opposition_place:str

    def generate_payroll(self) -> None:
        self.salary = self.base_salary + self.officer_complement

class Interim(Teacher):
    interim_complement:float
    destination:str

    def generate_payroll(self) -> None:
        self.salary = self.base_salary + self.interim_complement

class Substitute(Teacher):
    displacement:float
    initDate:date

    def generate_payroll(self) -> None:
        self.salary = self.base_salary + self.displacement

    @override
    def teach(self) ->None:
        print("Substitúo unha clase de programación en Python")