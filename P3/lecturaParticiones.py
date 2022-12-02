from io import open
from Particion import Particion

def lectura(nombre):
    lectura_particiones = open(nombre, "r")

    lista = lectura_particiones.readlines()

    lectura_particiones.close()

    particiones = []

    for particion in lista:
        elementos = particion.split()
        particiones.append(Particion(elementos[0],elementos[1],elementos[2],elementos[3]))

    particiones = sorted(particiones,key=lambda p : p.llegada)

    return particiones 
