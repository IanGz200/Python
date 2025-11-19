class Table:
    """
    Clase que dado un numero calcula la tabla de multiplicar del 1 al 10
    """
    number:int

    def __init__(self, number:int):
        """
        Constructor de la clase Table
        :param number: numero a calcular
        """
        self.number = number

    def show(self):
        """
        Metodo que muestra la tabla de multiplicar
        :return: tabla de "numero"
        """
        for i in range(0,11):
            print(self.number*i)

def main():
    """
    Metodo main
    :return: tabla de multiplicar
    """
    table = Table(int(input("Introduce numero: ")))
    table.show()

if __name__ == '__main__':
    main()