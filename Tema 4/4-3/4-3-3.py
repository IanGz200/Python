from abc import ABC, abstractmethod

class Speaker(ABC):

    @abstractmethod
    def speak(self)->None:
        pass

class Person(ABC):
    name:str
    age:int

    def __init__(self, name:str, age:int) -> None:
        self.name=name
        self.age=age

class Student(Person, Speaker):

    career:str
    course:int

    def __init__(self, name:str, age:int, career:str, course:int) -> None:
        super().__init__(name, age)
        self.career=career
        self.course=course

    def speak(self) -> None:
        pass

class Teacher(Person, Speaker):
    office:str
    email:str

    def __init__(self, name:str, age:int, office:str, email:str) -> None:
        super().__init__(name, age)
        self.office=office
        self.email=email

    def speak(self) -> None:
        pass

class Concierge(Person, Speaker):
    turn:str
    seniority:bool
    def __init__(self, name:str, age:int, turn:str, seniority:bool) -> None:
        super().__init__(name, age)
        self.turn=turn
        self.seniority=seniority

    def speak(self) -> None:
        pass

class Device(ABC):
    consumption:float
    price:float

    def __init__(self, consumption:float, price:float) -> None:
        self.consumption=consumption
        self.price=price

class Tv(Device, Speaker):
    teletext:bool
    inches:int

    def __init__(self, consumption:float, price:float, teletext:bool, inches:int) -> None:
        super().__init__(consumption, price)
        self.teletext=teletext
        self.inches=inches

    def speak(self) -> None:
        pass

class Radio(Device, Speaker):
    cassette:bool
    power:float

    def __init__(self, consumption:float, price:float, cassette:bool, power:float) -> None:
        super().__init__(consumption, price)
        self.cassette=cassette
        self.power=power

    def speak(self) -> None:
        pass

class WashingMachine(Device):
    height:float
    width:float

    def __init__(self, consumption:float, price:float, height:float, width:float) -> None:
        super().__init__(consumption, price)
        self.height=height
        self.width=width

class Bird(ABC):
    sex:str
    age:int

    def __init__(self, sex:str, age:int) -> None:
        self.sex = sex
        self.age=age

class Canary(Bird):
    sing:bool

    def __init__(self, sex:str, age:int, sing:bool) -> None:
        super().__init__(sex, age)
        self.sing=sing

class Tweety(Canary, Speaker):
    number_of_films:int

    def __init__(self, sex:str, age:int, sing:bool, number_of_films:int) -> None:
        super().__init__(sex, age, sing)
        self.number_of_films=number_of_films

    def speak(self) -> None:
        pass

class Parrot(Bird, Speaker):
    region:str
    color:str

    def __init__(self, sex:str, age:int, region:str, color:str) -> None:
        super().__init__(sex, age)
        self.region=region
        self.color=color

    def speak(self) -> None:
        print(f'Hola son un Loro e sei falar')


class Vulture(Bird):
    flight_speed:float
    weight:float

    def __init__(self, sex:str, age:int, flight_speed:float, weight:float) -> None:
        super().__init__(sex, age)
        self.flight_speed=flight_speed
        self.weight=weight
def main():
    parrot = Parrot("macho",40,"Africa","Azul")
    parrot.speak()

if __name__ == '__main__':
    main()