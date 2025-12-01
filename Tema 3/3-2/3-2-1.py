class Matrix:
    """
    Clase que implementa una matriz y metodos para hacer calculo entre estas
    """
    matrix:list[list[int]]

    def fill(self) -> None:
        self.matrix = []
        for row in range(3):
            self.matrix.append([])
            for col in range(3):
                self.matrix[row].append(int(input(f"Introduce el numero {row + 1},{col + 1}: ")))


    def sum(self,m2:'Matrix')->'Matrix':
        """
        Suma dos matrices casilla por casilla
        :param m2: Una matriz
        :return: La suma de ambas matrices
        """
        result = Matrix()
        result.matrix = []
        for row in range(len(self.matrix)):
            result.matrix.append([])
            for col in range(len(self.matrix[row])):
                result.matrix[row].append(self.matrix[row][col]+m2.matrix[row][col])

        return result

    def show(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                print(self.matrix[row][col], end=" ")
            print()

def main():
    print('Introduce os valores da primeira matriz:')
    m = Matrix()
    m.fill()
    print('Introduce os valores da segunda matriz:')
    m2 = Matrix()
    m2.fill()
    m.sum(m2).show()

if __name__ == "__main__":
    main()