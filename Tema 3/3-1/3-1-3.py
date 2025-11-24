class Statistics:
    """
    Clase que contiene una lista de numeros y un metodo para saber la mediana de estos
    """
    numbers:list[int] = []

    def __init__(self):
        self.__fill()

    def __fill(self)->None:
        """
        Metodo que rellena una lista con un numero impar de numeros
        :return:
        """
        elem = int(input("Introduce un numero impar:"))
        while elem%2 == 0:
            elem = int(input("Introduce un numero impar:"))

        for i in range(elem):
            self.numbers.append(int(input("Introduce un numero:")))

    def median(self)->str:
        """
        Metodo que calcula la mediana al calcular los numeros mayores y menores
        :return: La media de numbers
        """
        median:int = self.numbers[1]

        for i in range(len(self.numbers)):
            menores:int = 0
            mayores:int = 0
            for j in range(len(self.numbers)):
                if self.numbers[j] > self.numbers[i]:
                    mayores += 1
                if self.numbers[j] < self.numbers[i]:
                    menores += 1

            if menores == mayores:
                median = self.numbers[i]

        return f"La mediana es: {median}"

def main():
    stats = Statistics()
    print(stats.median())

if __name__ == "__main__":
    main()