class Marks:
    """
    Clase que almacena una lista de notas
    """
    notas:list[int] = []

    def __init__(self):
        self.__fill()

    def __fill(self)->None:
        """
        Rellena la lista con 10 notas
        """
        for i in range(10):
            self.notas.append(int(input(f"Introduce la nota numero {i+1}:")))

    def get_average(self)->float:
        """
        Devuelve la media de las notas de la clase
        :return: media de las notas
        """
        suma:int = 0
        for i in range(len(self.notas)):
            suma += self.notas[i]

        return suma / len(self.notas)



def main():
    marks = Marks()
    print(marks.get_average())

if __name__ == "__main__":
    main()