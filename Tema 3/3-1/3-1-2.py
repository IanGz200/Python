class StudentMarks:
    """
    Clase que guarda las notas de los alumnos y que contiene dos metodos para mostrar la mayor y la menor acompañadas
    del nombre del alumno
    """
    alumnos:list[str] = []
    notas:list[int] = []

    def __init__(self):
        """
        Constructor de la clase StudentMarks
        """
        self.__fill()

    def __fill(self):
        """
        Metodo que rellena los dos atributos de la clase con un nombre y su nota
        """
        for i in range(10):
            self.alumnos.append(input("Introduzca el nombre del alumno: "))
            self.notas.append(int(input(f"Introduzca la nota del alumno {self.alumnos[i]}: ")))

    def min(self):
        """
        Asigna la nota mas baja a una variable y el nombre correspondiente al alumno y lo devuelve
        :return: Nota y nombre del alumno con la nota mas baja
        """
        minim:int = 10
        minalumno = ""
        for i in range(len(self.notas)):
            if self.notas[i] < minim:
                minim = self.notas[i]
                minalumno = self.alumnos[i]

        return  f"El alumno con la nota mas alta es {minalumno}, con un: {minim}"

    def max(self):
        """
        Asigna la nota mas alta a una variable y el nombre correspondiente al alumno y lo devuelve
        :return: Nota y nombre del alumno con la nota mas alta
        """
        maxim:int = 0
        maxalumno = ""
        for i in range(len(self.notas)):
            if self.notas[i] > maxim:
                maxim = self.notas[i]
                maxalumno = self.alumnos[i]

        return  f"El alumno con la nota mas baja es {maxalumno}, con un: {maxim}"


def main():
    s = StudentMarks()
    print(s.min())
    print(s.max())

if __name__ == "__main__":
    main()
