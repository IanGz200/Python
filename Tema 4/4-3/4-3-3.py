from abc import ABC, abstractmethod

class Person(ABC):
    name:str
    age:int

    def __init__(self, name:str, age:int) -> None:
        self.name=name
        self.age=age