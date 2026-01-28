from datetime import datetime,date
from abc import abstractmethod, ABC

class Teacher(ABC):
    name:str
    surname:str
    address:str
    base_salary:float
    salary:float

    def __init__(self, name:str, surname:str, address:str, base_salary:float):
        self.name=name
        self.surname=surname
        self.address=address
        self.base_salary=base_salary

    def teach(self)->None:
        print("Dou unha clase de programación en Python")

    @abstractmethod
    def generate_payroll(self)->None:
        pass

class CareerOfficer(Teacher):
    officer_complement:float
    opposition_year:int
    opposition_place:str

    def __init__(self, name:str, surname:str, address:str, base_salary:float, officer_complement, opposition_year:int, opposition_place:str):
        super().__init__(name, surname, address, base_salary)
        self.officer_complement=officer_complement
        self.opposition_year=opposition_year
        self.opposition_place=opposition_place

    def generate_payroll(self) -> None:
        self.salary = self.base_salary + self.officer_complement

class Interim(Teacher):
    interim_complement:float
    destination:str

    def __init__(self, name:str, surname:str, address:str, base_salary:float, interim_complement, destination:str):
        super().__init__(name,surname,address,base_salary)
        self.interim_complement=interim_complement
        self.destination=destination

    def generate_payroll(self) -> None:
        self.salary = self.base_salary + self.interim_complement

class Substitute(Teacher):
    displacement:float
    init_date:date

    def __init__(self, name:str, surname:str, address:str, base_salary:float, displacement:float, init_date:date):
        super().__init__(name, surname, address, base_salary)
        self.displacement=displacement
        self.init_date=init_date

    def generate_payroll(self) -> None:
        self.salary = self.base_salary + self.displacement

    def teach(self) ->None:
        print("Substitúo unha clase de programación en Python")

def main():
    career_officer = CareerOfficer("Carlos","Ocelote","calle x",1500, 300, 2020, "Salvaterra de Miño")
    interim = Interim("Javier", "Prades Batalla", "calle y", 1300, 200, "Berlín")
    substitute = Substitute("Daniel", "Pérez", "calle z", 1300, 50, date(2026, 1, 28))
    career_officer.generate_payroll()
    interim.generate_payroll()
    substitute.generate_payroll()
    print(f'Chámome {career_officer.name} e o meu salario é de {career_officer.salary}')
    career_officer.teach()
    print(f'Chámome {interim.name} e o meu salario é de {interim.salary}')
    interim.teach()
    print(f'Chámome {substitute.name} e o meu salario é de {substitute.salary}')
    substitute.teach()

if __name__ == "__main__":
    main()