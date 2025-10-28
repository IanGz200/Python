class Mayor:
    """
    Clase que recive tres numeros.
    Contiene un metodo que recibiendo tres ints devuelve el mayor de ellos
    """
    def __init__(self, uno: int, dos: int, tres: int):
        """
        Constructor de Mayor
        :param uno: numero uno
        :param dos: numero dos
        :param tres: numero tres
        """
        self.n1:int = uno
        self.n2:int = dos
        self.n3:int = tres

    def numero_mayor(self)->int:
        """
        Comprueba el mayor de tres números
        :return: El mayor
        """
        if self.n1 >= self.n2 and self.n1 >= self.n3:
            return self.n1
        elif self.n2 >= self.n3:
            return self.n2
        else:
            return self.n3

def main():
    """
    Main que pide por pantalla tres numeros con los que crear una clase y mostrar el mayor de ellos
    """
    mayor = Mayor(int(input("Introduce el primer número: ")),int(input("Introduce el segundo número: ")),int(input("Introduce el tercer número: ")))
    print("El numero mas grande es:",mayor.numero_mayor())

if __name__ == '__main__':
    main()