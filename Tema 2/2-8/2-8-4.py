class WorkingDay:
    """
    Clase que permite calcular el salario semanal de un trabajador
    """
    quenda:str
    dia:str
    horas:int
    def __init__(self, quenda:str, dia:bool, horas:int):
        self.quenda = quenda
        if dia:
            self.dia = "d"
        else:
            self.dia = "x"
        self.horas = horas

    def salary(self)->float:
        """
        Metodo que calcula el salario semanal dependiendo de las condiciones del contrato.
        :return: salario semanal
        """
        if self.quenda == "d":
            if self.dia == "d":
                return (self.horas*8*4)+(self.horas*8*1.2)
            else:
                return self.horas*8*5
        else:
            if self.dia == "d":
                return (self.horas*12*4)+(self.horas*12*1.2)
            else:
                return self.horas*12*5

def main():
    wd1 = WorkingDay("d",True,8)
    wd2 = WorkingDay("d",False,8)
    wd3 = WorkingDay("n",True,8)
    wd4 = WorkingDay("n",False,8)
    print("El salario diurno con domingo es:",wd1.salary())
    print("El salario diurno sin domingo es:",wd2.salary())
    print("El salario nocturno con domingo es:",wd3.salary())
    print("El salario nocturno sin domingo es:",wd4.salary())

if __name__ == '__main__':
    main()