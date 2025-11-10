qualification:int = int(input("Introduce la nota: "))

match qualification:
    case 10:
        print("Matricula de honor")
    case 9:
        print("Sobresaliente")
    case x if x >= 7:
        print("Notable")
    case 6:
        print("Bien")
    case 5:
        print("Aprobado")
    case _:
        print("Suspenso")