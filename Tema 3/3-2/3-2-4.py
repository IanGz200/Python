import random

class AdventCalendar:
    """
    Clase que simula un calendario de adviento que va comiendose cada dia por orden hasta que llegue la navidad
    """
    matriz:list[list[int]] = [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]
    MAX:int = 24
    numbers:list[int] = []
    min:int = 1
    ROWS:int = 4
    COLUMNS:int = 6

    def show(self)->None:
        """
        Muestra cada posicion de la matriz
        :return: cada posicion de la matriz por pantalla
        """
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                print(self.matriz[i][j],end=" ")
            print("")
        print("")


    def fill(self)->None:
        """
        Recorre la matriz rellenandola de numeros del 1 al 24 asegurandose de que no exista ya una posicion con ese numero
        """
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                self.matriz[i][j] = random.randrange(0,self.MAX)+1
                while self.matriz[i][j] in self.numbers:
                    self.matriz[i][j] = random.randrange(0,self.MAX)+1
                self.numbers.append(self.matriz[i][j])

    def christmas_is_here(self)->bool:
        """
        En caso de que toda la matriz este a 0 se devuelve que la navidad ya esta aqui con un true
        :return: True en caso de tener toda la matriz a 0s o false al no tenerla
        """
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if self.matriz[i][j] != 0:
                    return False
        return True

    def eat(self)->None:
        """
        Convierte en 0 el numero mas pequeño de la matriz
        """
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if self.matriz[i][j] == self.min:
                    self.matriz[i][j] = 0
        self.min += 1

def main():
    ac = AdventCalendar()
    ac.fill()
    ac.show()
    while not ac.christmas_is_here():
        ac.eat()
        ac.show()

if __name__ == "__main__":
    main()