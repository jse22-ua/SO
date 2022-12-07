from io import open
from Particion import Particion

def lectura(fichero):
    lectura_procesos = open(fichero, "r")

    lista = lectura_procesos.readlines()

    lectura_procesos.close()

    procesos = []

    for proceso in lista:
        elementos = proceso.split()
        procesos.append(Particion(elementos[0],elementos[1],elementos[2],elementos[3]))

    procesos = sorted(procesos,key=lambda p : p.llegada)

    return procesos

def escribir(fichero, paraEscribir):
    escribir_particiones = open(fichero,"a")

    escribir_particiones.write(paraEscribir)

    escribir_particiones.close()