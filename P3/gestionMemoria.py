from os import remove, path
from manejarArchivos import *
from Particion import Particion
from Vacio import Vacio
from turtle import *


MEMORIA_TOTAL = 2000

lista_procesos = lectura("procesos.txt")

memoria=[]

#Si la memoria esta vacia no hace falta comprobar que hueco se ajusta mejor 
#Asi que esta funcion añade mientas quepa en el unico hueco
# devuelve aquellos procesos que no cupieron
def siMemoriaVacia(lista):
    sobras = []
    cuenta = 0
    for proceso in lista:
        if(cuenta+int(proceso.memoria)<MEMORIA_TOTAL):
            memoria.append((cuenta,proceso))
            cuenta += int(proceso.memoria)
        else:
            sobras.append(proceso)
    if(MEMORIA_TOTAL-cuenta>0):
        memoria.append((cuenta,Vacio(MEMORIA_TOTAL-cuenta)))
        
    return sobras

#Esta funcion elimina procesos de memoria que cuyo tiempo ejecucion == 0
def limpiarmemoria():
    if(len(memoria)!=0):
        cuenta=0
        for par in memoria:
            posicion = par[0]
            proceso = par[1]
            if(type(proceso)==Particion):
                if(int(proceso.Tejecucion)==0):
                    memoria.remove(par)
                    memoria.insert(cuenta,(posicion,Vacio(int(proceso.memoria))))
            cuenta +=1

#esta funcion resta uno al tiempo de ejecucion si es una clase particion
def pasaTiempo(proceso):
    if(type(proceso)==Particion):
        proceso.restarTiempo()

#Este funcion filtra los huecos que tienen >= tamaño al proceso que queremos insertar
#devuelve el indice del hueco en memoria y el hueco
def decidirHueco(tamanyo,tipohueco):
    hueco = ()
    lista_position = list(map(lambda x : (memoria.index(x),x),memoria))
    vacios_filtrados = list(filter(lambda y : type(y[1][1])==Vacio and int(y[1][1].memoria)>=tamanyo,lista_position))
    if(len(vacios_filtrados)!=0):
        hueco = vacios_filtrados[0]
        for vacio in vacios_filtrados:
            if(tipohueco=='1'):#mejorhueco
                if(int(hueco[1][1].memoria)>int(vacio[1][1].memoria)):
                    hueco = vacio
            else:#peorhueco
                if(int(hueco[1][1].memoria)<int(vacio[1][1].memoria)):
                    hueco = vacio
    return hueco

#Esta funcion recorre una lista de procesos
#elimina el hueco devuelto por decidirhueco()
#y añade el proceso y el hueco que sobra
#devuelve los procesos que no caben en ningun hueco se añade a sobras
def addProcesos(lista,tipohueco):
    sobras = []
    if(len(memoria)==0):
      sobras = siMemoriaVacia(lista) 
    else:
        for proceso in lista:
            unirhuecos()
            tamanyo = int(proceso.memoria)
            hueco = decidirHueco(tamanyo,str(tipohueco))
            if(len(hueco)!=0):
                indice = int(hueco[0])
                proc= hueco[1]
                memoria.remove(proc)
                memoria.insert(indice,(proc[0],proceso))
                if(int(proc[1].memoria)-tamanyo>0):
                    memoria.insert(indice+1,(proc[0]+tamanyo,Vacio(int(proc[1].memoria)-tamanyo)))
            else:
                sobras.append(proceso)
            

    return sobras

#esta funcion recorre memoria y 
#se encarga de que no haya dos huecos consecutivos
def unirhuecos():
    if(len(memoria)!=0):
        vacio = memoria[0]
        count = 0
        while count < len(memoria):
            if(count==0):
                count+=1
            elif(type(vacio[1])==Vacio and type(memoria[count][1])==Vacio):
                vacio[1].memoria+=memoria[count][1].memoria
                memoria.remove(memoria[count])
            else:
                vacio = memoria[count]
                count +=1


#Esta funcion devuelve una cadena con la estructura que debe
# escribir en un fichero en cada iteracion
def cadenaAEscribir(iteracion):
    cadena = str(iteracion) + " "
    for particion in memoria:
        cadena += "[" + str(particion[0]) 
        cadena += " " + particion[1].nombre
        cadena += " " + str(particion[1].memoria) + "] "
    cadena += "\n"
    
    return cadena

######################
##                  ##
##  Parte grafica   ##
##                  ##
######################

#esta funcion escribe la medida en negro y 
# vuelve a poner el color de la linea anterior
def escribirMedida(valor,colorlapiz,colorfondo):
    color('black')
    write(valor)
    color(colorlapiz,colorfondo)

#esta funcion dibuja la memoria vacia
def dibujarMemoriaVacia():
    color('yellow','yellow')
    penup()
    home()
    setpos(-200,200)
    begin_fill()
    pendown()
    fd(200)
    escribirMedida(0,'yellow','yellow')
    right(90)
    fd(400)
    escribirMedida(2000,'yellow','yellow')
    right(90)
    fd(200)
    right(90)
    fd(400)
    right(90)
    end_fill()

#devuelve una tupla con el inicio del proceso y el tamaño 
#a la escala del dibujo
def ajustarEscala(posicion,tamanyo):
    inicio = (posicion*400)/2000
    tam = (tamanyo*400)/2000
    return (inicio,tam)

#dibuja el proceso
def dibujarProceso(particion):
    setpos(-200,200)
    right(90)
    dimensiones = ajustarEscala(int(particion[0]),int(particion[1].memoria))
    fd(dimensiones[0])
    left(90)
    fd(1)
    pendown()
    begin_fill()
    fd(198)
    escribirMedida(particion[0],'yellow','blue')
    right(90)
    fd(dimensiones[1])
    right(90)
    fd(99)
    write(particion[1].nombre,align='center',font=("Verdana",15, "normal"))
    fd(99)
    right(90)
    fd(dimensiones[1])
    end_fill()


#lo dibuja todo
def dibujarmemoria():
    clear()
    dibujarMemoriaVacia()
    left(90)
    color('yellow','blue')
    for particion in memoria:
        penup()
        home()
        if(type(particion[1])==Particion):
           dibujarProceso(particion)
        else:
            setpos(0,200)
            right(90)
            dimensiones = ajustarEscala(int(particion[0]),int(particion[1].memoria))
            fd(dimensiones[0])
            pendown()
            escribirMedida(particion[0],'yellow','yellow')
            

def ejecutar(tipohueco):
    hideturtle()
    sobras = []
    count = 0
    speed(15)
    if(path.isfile("particiones.txt")):
        remove("particiones.txt")
    while len(memoria)!=1:
        count+=1
        lista_proc = list(filter(lambda x : int(x.llegada)==count , lista_procesos))
        for sobra in sobras :
            lista_proc.append(sobra)
        sobras.clear()
        lista_proc = sorted(lista_proc,key=lambda p : p.llegada)
    
        for proceso in memoria:
            pasaTiempo(proceso[1])
    

        limpiarmemoria()
        sobras = addProcesos(lista_proc,tipohueco)
        cadena = cadenaAEscribir(count)
        escribir("particiones.txt",cadena)
        dibujarmemoria()
        input("Presiona ENTER para pasar a la siguiente iteracion")

while True:
    print("Gestion de memoria")
    print("------------------\n")
    print("Selecciona una opcion:")
    print("1. Mejor hueco")
    print("2. Peor hueco")
    print("Opcion: ")
    opcion = input()

    print("Seleccionaste la opcion: ")

    if opcion == '1':
        print("Mejor hueco")
        break
    if opcion == '2':
        print("Peor hueco")
        break
    if opcion != '2' or opcion != '1':
        print("Error")


ejecutar(opcion)
salir = input("Presiona ENTER para salir")
exit(salir)
mainloop()