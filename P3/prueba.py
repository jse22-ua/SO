from Particion import Particion
lista_particiones = [
    Particion("P1", 1, 500, 3),
    Particion("P2", 2, 300, 2),
    Particion("P3", 3, 200, 3),
    Particion("P4", 4, 100, 1),
    Particion("P5", 2, 400, 1),
    Particion("P6", 3, 500, 4)
]

ordenados = sorted(lista_particiones, key=lambda p: p.llegada)

for proceso in ordenados:
    print(proceso.nombre)
