import lecturaParticiones
from Particion import Particion

lista_particiones = lecturaParticiones.lectura("particiones.txt")

for particion in lista_particiones:
    print(particion.toString())