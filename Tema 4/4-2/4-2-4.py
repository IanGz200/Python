from datetime import datetime,date
from abc import abstractmethod, ABC

class HighSchool:
    """
    Clase que representa un instituto y contiene un nombre y una lista de los profesores que trabajan en el
    """
    name:str
    teachers:list['Teacher']

    def __init__(self, name:str):
        self.name = name
        self.teachers = []

    def most_paid(self)->'Teacher':
        """
        Metodo que utilizado para recorrer la lista de profesores y obtener el del salario mas bajo
        :return: El profesor mejor pagado
        """
        most_paid = self.teachers[0].salary
        most_paid_teacher:Teacher = self.teachers[0]
        for teacher in self.teachers:
            if teacher.salary > most_paid:
                most_paid = teacher.salary
                most_paid_teacher = teacher

        return most_paid_teacher

    def least_paid(self)->'Teacher':
        """
        Metodo que utilizado para recorrer la lista de profesores y obtener el del salario mas bajo
        :return: El profesor peor pagado
        """
        least_paid = self.teachers[0].salary
        least_paid_teacher: Teacher = self.teachers[0]
        for teacher in self.teachers:
            if teacher.salary < least_paid:
                least_paid = teacher.salary
                least_paid_teacher = teacher

        return least_paid_teacher

    def salary_cost(self)->float:
        """
        Metodo usado para calcular el coste total de los salarios de los profesores
        :return: El coste total
        """
        coste = 0
        for teacher in self.teachers:
            coste += teacher.salary

        return coste

    def salary_average(self)->float:
        """
        Metodo usado para calcular el coste medio de los salarios de los profesores
        :return: La media de los salarios
        """
        average = 0
        count = 0
        for teacher in self.teachers:
            average += teacher.salary
            count += 1
        return average / count

class Teacher(ABC):
    """
    Clase que representa a un profesor
    """
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
        """
        Metodo que devuelve por pantalla informacion sobre la ocupacion del profesor
        """
        print("Dou unha clase de programación en Python")

    @abstractmethod
    def generate_payroll(self)->None:
        """
        Metodo que se heredara a las subclases para generar los salarios de estas en base a sus atributos
        """
        pass

class CareerOfficer(Teacher):
    """
    Subclase de Teacher
    """
    officer_complement:float
    opposition_year:int
    opposition_place:str

    def __init__(self, name:str, surname:str, address:str, base_salary:float, officer_complement, opposition_year:int, opposition_place:str):
        super().__init__(name, surname, address, base_salary)
        self.officer_complement=officer_complement
        self.opposition_year=opposition_year
        self.opposition_place=opposition_place

    def generate_payroll(self) -> None:
        """
        Genera el salario en base al salario base y el complemento
        """
        self.salary = self.base_salary + self.officer_complement

class Interim(Teacher):
    """
    Subclase de Teacher
    """
    interim_complement:float
    destination:str

    def __init__(self, name:str, surname:str, address:str, base_salary:float, interim_complement, destination:str):
        super().__init__(name,surname,address,base_salary)
        self.interim_complement=interim_complement
        self.destination=destination

    def generate_payroll(self) -> None:
        """
        Genera el salario en base al salario base y el complemento
        """
        self.salary = self.base_salary + self.interim_complement

class Substitute(Teacher):
    """
    Subclase de Teacher
    """
    displacement:float
    init_date:date

    def __init__(self, name:str, surname:str, address:str, base_salary:float, displacement:float, init_date:date):
        super().__init__(name, surname, address, base_salary)
        self.displacement=displacement
        self.init_date=init_date

    def generate_payroll(self) -> None:
        """
        Genera el salario en base al salario base y el desplazamiento
        """
        self.salary = self.base_salary + self.displacement

    def teach(self) ->None:
        print("Substitúo unha clase de programación en Python")

def main():
    #Se generan los objetos con sus atributos
    hs = HighSchool("Pazo da Mercé")
    career_officer = CareerOfficer("Carlos", "Ocelote", "calle x", 1500, 300, 2020, "Salvaterra de Miño")
    interim = Interim("Javier", "Prades Batalla", "calle y", 1300, 200, "Berlín")
    substitute = Substitute("Daniel", "Pérez", "calle z", 1300, 50, date(2026, 1, 28))
    #Se generan los salarios
    career_officer.generate_payroll()
    interim.generate_payroll()
    substitute.generate_payroll()
    #Añade los objetos profesor creados a la lista de highschool
    hs.teachers.append(career_officer)
    hs.teachers.append(interim)
    hs.teachers.append(substitute)
    #Se referencian los 4 metodos de highschool y se saca la información por pantalla
    print('El profesor mejor pagado es: ' + hs.most_paid().name)
    print('El profesor peor pagado es: ' + hs.least_paid().name)
    print(f'El coste total de los salarios es: {hs.salary_cost()}')
    print(f'La media de los salarios es de: {hs.salary_average()}')

if __name__ == "__main__":
    main()