class SortedArray:
    """
    Clase que contiene una lista y los metodos para llenarlo, ordenarlo y mostrarlo
    """

    valores:list

    def fill(self)->None:
        """
        Inicializa la lista de valores y asigna los valores por pantalla
        """
        self.valores = []
        for i in range(6):
            self.valores.append(int(input("Introduce un numero:")))

    def sort(self)->None:
        """
        Ordena los valores de la lista con el metodo bubble sort
        """
        for i in range(len(self.valores)-1):
            for j in range(len(self.valores)-i-1):
                if self.valores[j] > self.valores[j+1]:
                    """
                    Intercambia los valores
                    """
                    self.valores[j], self.valores[j+1] = self.valores[j+1],self.valores[j]

    def show(self)->None:
        """
        Muestra los valores por pantalla
        """
        print(self.valores)

def main():
    sort = SortedArray()
    sort.fill()
    sort.sort()
    sort.show()

if __name__ == "__main__":
    main()