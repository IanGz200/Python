class Pen:
    """
    Clase que representa un boligrafo con tinta que se gasta al escribir
    """
    ink:int = 30

    def write(self,num):
        """
        Metodo que reduce la tinta al escribir una palabra
        :param num: el numero de palabras
        :return: las palabras escritas o la falta de tinta para escribirlas
        """
        for i in range(num):
            if self.ink>0:
                print("Hola")
                self.ink-=1
        if self.ink==0:
            print("No queda tinta")

def main():
    pen = Pen()
    pen.write(20)
    pen.write(15)
    pen.write(6)

if __name__ == "__main__":
    main()