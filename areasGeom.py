from math import pi

def area_ret(ladoA, ladoB):

    area = ladoA * ladoB

    return area

def area_circ(diametro):

    area = pi * (diametro ** 2) / 4

    return area

def area_triang(base, altura):

    area = base * altura / 2

    return area