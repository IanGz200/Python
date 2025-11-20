class StudentMarks:
    alumnos:list[str] = []
    notas:list[int] = []

    def __init__(self):
        self.__fill()

    def __fill(self):
        for i in range(10):
            self.alumnos.append(input("Introduzca el nombre del alumno: "))
            self.notas.append(int(input(f"Introduzca la nota del alumno {self.alumnos[i]}: ")))

def main():
    s = StudentMarks()

if __name__ == "__main__":
    main()
