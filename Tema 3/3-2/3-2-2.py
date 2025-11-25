class Matrix:
    """
    Clase que implementa una matriz y metodos para hacer calculo entre estas
    """
    matrix:list[list[int]]=[[0,0,0],[0,0,0],[0,0,0]]

    def __init__(self) -> None:
        for row in range(3):
            for col in range(3):
                self.matrix[row][col] = int(input(f"Introduce el numero {row + 1},{col + 1}: "))


    def sum(self,m2)->list[list[int]]:
        """
        Suma dos matrices casilla por casilla
        :param m2: Una matriz
        :return: La suma de ambas matrices
        """
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                self.matrix[row][col] += m2[row][col]

        return self.matrix

    def substract(self,m2)->list[list[int]]:
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
    m = Matrix()
    m2 = Matrix()
    print(m.sum(m2.matrix))

if __name__ == "__main__":
    main()