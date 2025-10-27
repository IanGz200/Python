class Person:
    """
    Clase que recibe los datos de una persona por pantalla
    """
    def __init__(self):
        """
        Constructor de la clase Person
        Pide el nombre y año de nacimiento por pantalla
        """
        self.name = input("Nombre: ")
        self.birthYear = int(input("Año de nacimiento: "))

    def future(self):
        """
        Muestra la edad de la persona en 2030 por pantalla
        """
        print("Son ", self.name," e no ano 2030 terei ", 2030-self.birthYear," anos.")

def main():
    """
    Crea dos personas
    :return: Muestra por pantalla la edad en 2030
    """
    p1 = Person()
    p2 = Person()
    p1.future()
    p2.future()

if __name__ == "__main__":
    main()