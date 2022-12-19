from io import open
from Particion import Particion

#Lee un fichero con el nombre de fichero y devuelve una lista de procesos
def lectura(fichero):
    lectura_procesos = open(fichero, "r")

    lista = lectura_procesos.readlines()

    lectura_procesos.close()

    procesos = []

    for proceso in lista:
        elementos = proceso.split()
        procesos.append(Particion(elementos[0],elementos[1],elementos[2],elementos[3]))

    #ordena la lista por tiempo de llegada antes de devolverla
    procesos = sorted(procesos,key=lambda p : p.llegada)
    return procesos

#Escribe un fichero o añade a un fichero ya existente
#los datos de paraEscribir
def escribir(fichero, paraEscribir):
    escribir_particiones = open(fichero,"a")

    escribir_particiones.write(paraEscribir)

    escribir_particiones.close()