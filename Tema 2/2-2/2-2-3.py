class Circle:
    """
    Clase circulo que contiene el valor del radio
    """
    def __init__(self, radius:float):
        """
        Constructor
        En caso de que el valor del radio sea mayor de MAX_RADIUS lo vuelve a pedir
        :param radius: radio de la circunferencia
        """
        self.MAX_RADIUS:int = 10
        self.radius:float = radius
        while self.radius > self.MAX_RADIUS:
            self.radius:float = int(input("Introduce un valor menor o igual a 10 para el radio: "))


    def show(self)-> str:
        """
        Metodo diseñado para mostrar el radio del circulo por pantalla
        :return: radio
        """
        return "Son un dirculo con radio: " + str(self.radius)

    def enlarge(self):
        """
        Este metodo agranda los radios por 2 en caso de no superar MAX_RADIUS
        """
        if self.radius*2 <= self.MAX_RADIUS:
            self.radius = self.radius * 2

def main():
    """
    Muestra el valor del radio de ambas circunferencias despues de intentar agrandarlo
    """
    c1 = Circle(3)
    c2 = Circle(10)
    c1.enlarge()
    c2.enlarge()

    print(c1.show())
    print(c2.show())


if __name__ == "__main__":
    main()