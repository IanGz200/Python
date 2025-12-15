class Statistics:
    """
    Clase que contiene una lista de numeros y un metodo para saber la mediana de estos
    """
    numbers:list[int]

    def __init__(self):
        self.__fill()

    def __fill(self)->None:
        """
        Metodo que rellena una lista con un numero impar de numeros
        :return:
        """
        self.numbers = []
        elem = int(input("Introduce un numero impar:"))
        while elem%2 == 0:
            elem = int(input("Introduce un numero impar:"))

        for i in range(elem):
            self.numbers.append(int(input("Introduce un numero:")))

    def median(self)->int:
        """
        Metodo que calcula la mediana con el metodo insert sort
        :return: La mediana de numbers
        """
        for i in range(1, len(self.numbers)):
            key = self.numbers[i]
            j = i - 1

            while j >= 0 and self.numbers[j] > key:
                self.numbers[j + 1] = self.numbers[j]
                j -= 1

            self.numbers[j + 1] = key

        return self.numbers[len(self.numbers) // 2]

def main():
    stats = Statistics()
    print("La mediana es:",stats.median())

if __name__ == "__main__":
    main()