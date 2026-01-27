class Matrix:
    """
    Clase que implementa una matriz y metodos para hacer calculo entre estas
    """
    matrix: list[list[int]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self, default_values: bool = None) -> None:
        if default_values is None:
            for row in range(3):
                for col in range(3):
                    self.matrix[row][col] = int(input(f"Introduce el numero {row + 1},{col + 1}: "))
        elif default_values:
            for row in range(3):
                for col in range(3):
                    self.matrix[row][col] = row + col

    def sumar(self, m2:list[list[int]] = None, m3:list[list[int]] = None) -> list[list[int]]:
        """
        Metodo que suma las matrices pasadas como parametros o en caso de no pasar ninguna se suma consigo misma
        :param m2: Una matriz
        :param m3: Una matriz
        :return: La suma de las matrices
        """
        if m2 is None:
            #En caso de no recibir ninguna matriz se sumara consigo misma
            for row in range(len(self.matrix)):
                for col in range(len(self.matrix[row])):
                    self.matrix[row][col] += self.matrix[row][col]
        else:
            if m3 is None:
                for row in range(len(self.matrix)):
                    for col in range(len(self.matrix[row])):
                        self.matrix[row][col] += m2[row][col]
            else:
                #En caso de recibir dos matrices se sumaran las tres
                for row in range(len(self.matrix)):
                    for col in range(len(self.matrix[row])):
                        self.matrix[row][col] += m2[row][col] + m3[row][col]

        return self.matrix


    def substract(self, m2) -> list[list[int]]:
        """
        Substra dos matrices casilla por casilla
        :param m2: Una matriz
        :return: La resta de ambas matrices
        """
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                self.matrix[row][col] -= m2[row][col]

        return self.matrix


def main():
    m = Matrix(True)
    m2 = Matrix(True)
    m3 = Matrix(True)
    print(m.matrix)
    print(m2.matrix)
    print(m3.matrix)
    print(m.sumar(m2.matrix, m3.matrix))


if __name__ == "__main__":
    main()
