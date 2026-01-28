from abc import abstractmethod, ABC

class Shape(ABC):
    """
    Clase abstracta que define los metodos de creacion y borrado de figuras
    """

    @abstractmethod
    def draw(self)->None:
        """
        Metodo que simula el dibujo de una forma
        """
        pass

    @abstractmethod
    def erase(self)->None:
        """
        Metodo que simula el borrado de una forma
        """
        pass

class Square(Shape):
    """
    Subclase de Shape que representa un cuadrado
    """
    def erase(self) -> None:
        """
        Muestra por pantalla el borrado del cuadrado
        """
        print("Borrando cuadrado")

    def draw(self) -> None:
        """
        Muestra por pantalla el dibujado del cuadrado
        """
        print("Dibujando cuadrado")

class Triangle(Shape):
    """
    Subclase de Shape que representa un triangulo
    """
    def erase(self) -> None:
        """
        Muestra por pantalla el borrado del triangulo
        """
        print("Borrando Triangulo")

    def draw(self) -> None:
        """
        Muestra por pantalla el dibujado del triangulo
        """
        print("Dibujando Triangulo")

class Circle(Shape):
    """
    Subclase de Shape que representa un circulo
    """
    def erase(self) -> None:
        """
        Muestra por pantalla el borrado del circulo
        """
        print("Borrando Circulo")

    def draw(self) -> None:
        """
        Muestra por pantalla el dibujado del circulo
        """
        print("Dibujando Circulo")

class Board:
    """
    Clase que representa un encerado y guarda una lista de formas
    """
    shapes:list['Shape']

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape:Shape) -> None:
        """
        Metodo usado para añadir formas a la lista
        :param shape: Forma a añadir
        """
        self.shapes.append(shape)
        shape.draw()

    def erase_shapes(self) -> None:
        """
        Metodo usado para borrar todas las formas guardadas en la lista
        """
        for shape in self.shapes:
            shape.erase()
        self.shapes.clear()

def main():
    square = Square()
    triangle = Triangle()
    circle = Circle()
    board = Board()
    board.add_shape(square)
    board.add_shape(triangle)
    board.add_shape(circle)
    board.erase_shapes()

if __name__ == '__main__':
    main()