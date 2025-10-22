class Circle:
    """
    Clase circulo que contiene el valor del radio
    """
    def __init__(self, radius:float):
        """
        Constructor
        :param radius: radio de la circunferencia
        """
        self.radius:float= radius


    def show(self)-> str:
        """
        Metodo diseñado para mostrar el radio del circulo por pantalla
        :return: radio
        """
        return "Son un dirculo con radio: " + str(self.radius)

def main():
    """
    Muestra el valor del radio de ambas circunferencias
    :return:
    """
    c1 = Circle(3)
    c2 = Circle(9)

    print(c1.show())
    print(c2.show())


if __name__ == "__main__":
    main()