class SortedArray:
    """
    Clase que contiene una lista y los metodos para llenarlo, ordenarlo y mostrarlo
    """

    valores: list
    sorted: bool

    def __init__(self):
        self.sorted = False

    def fill(self) -> None:
        """
        Inicializa la lista de valores y asigna los valores por pantalla
        """
        self.valores = []
        for i in range(6):
            self.valores.append(int(input("Introduce un numero:")))

    def sort(self) -> None:
        """
        Ordena los valores de la lista con el metodo bubble sort
        """
        for i in range(len(self.valores) - 1):
            for j in range(len(self.valores) - i - 1):
                if self.valores[j] > self.valores[j + 1]:
                    """
                    Intercambia los valores
                    """
                    self.valores[j], self.valores[j + 1] = self.valores[j + 1], self.valores[j]

        self.sorted = True

    def show(self) -> None:
        """
        Muestra los valores por pantalla
        """
        print(self.valores)

    def contains(self,number:int) -> bool:
        """
        Comprueba si un numero esta dentro de la lista, en caso de no estar ordenado se ordena
        :param number: numero a buscar
        :return: Si esta o no
        """

        if not self.sorted:
            self.sort()

        principio:int = 0
        final:int = len(self.valores)-1

        while principio <= final:
            medio = (principio + final) //2
            valor_medio = self.valores[medio]

            if valor_medio == number:
                return True
            elif valor_medio < number:
                principio = medio + 1
            else:
                final = medio - 1

        return False



def main():
    sort = SortedArray()
    sort.fill()
    sort.show()
    sort.sort()
    sort.show()
    number = int(input("Introduce un numero para buscar en el array:"))
    print("Contine el numero"if sort.contains(number) else "No contiene el numero")


if __name__ == "__main__":
    main()