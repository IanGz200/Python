class Mayor:
    """
    Clase que recive tres numeros.
    Contiene un metodo que recibiendo tres ints devuelve el mayor de ellos
    """

    uno:int
    dos:int
    tres:int

    def __init__(self, uno: int, dos: int, tres: int):
        """
        Constructor de Mayor
        :param uno: numero uno
        :param dos: numero dos
        :param tres: numero tres
        """
        self.uno = uno
        self.dos = dos
        self.tres = tres

    def numero_mayor(self)->int:
        """
        Comprueba el mayor de tres números
        :return: El mayor
        """
        if self.uno >= self.dos and self.uno >= self.tres:
            return self.uno
        elif self.dos >= self.tres:
            return self.dos
        else:
            return self.tres

def main():
    """
    Main que pide por pantalla tres numeros con los que crear una clase y mostrar el mayor de ellos
    """
    mayor = Mayor(
        int(input("Introduce el primer número: ")),
        int(input("Introduce el segundo número: ")),
        int(input("Introduce el tercer número: "))
    )

    print("El numero mas grande es:",mayor.numero_mayor())

if __name__ == '__main__':
    main()