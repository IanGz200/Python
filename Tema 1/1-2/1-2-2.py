from math import trunc

"""
Clase que devuelve segundos en formato hora minutos y segundos
"""
class Segundos:

    segundos:int=325

    horas:int =trunc(segundos/3600)

    minutos:int = trunc(segundos%3600/60)

    seg2:int = segundos%3600%60

    #Muestra por pantalla los segundos en horas, minutos y segundos
    print(segundos,"son",horas,"horas,",minutos,"minutos y",seg2,"segundos")