class Bigger:
    """
    Clase que contiene un metodo que pidiendo por pantalla 10 numeros duvuelve el mas grande
    """
    bigger:int = 0

    def getBigger(self)->str:
        """
        Almacena el numero si es mas grande que el ya almacenado
        :return: numero mayor
        """
        for i in range(10):
            temp:int = int(input("Introduce un numero:"))
            if temp> self.bigger:
                self.bigger = temp

        return f"El numero mas grande es: {self.bigger}"

def main():
    bigger = Bigger()
    print(bigger.getBigger())

if __name__ == "__main__":
    main()
