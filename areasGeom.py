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

def perim_triang(lado1, lado2, lado3):

    perim = lado1 + lado2 + lado3

    return perim

