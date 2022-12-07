
from manejarArchivos import *
from Particion import Particion
from Vacio import Vacio


MEMORIA_TOTAL = 2000

lista_procesos = lectura("procesos.txt")

memoria=[]

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

def limpiarmemoria():
    if(len(memoria)!=0):
        cuenta=0
        for par in memoria:
            posicion = par[0]
            proceso = par[1]
            if(type(proceso)==Particion):
                if(int(proceso.Tejecucion)==0):
                    memoria.remove(par)
                    memoria.insert(cuenta,(posicion,Vacio(proceso.memoria)))
            cuenta +=1

def pasaTiempo(proceso):
    if(type(proceso)==Particion):
        proceso.restarTiempo()

def mejorHueco(tamanyo):
    hueco = ()
    lista_position = list(map(lambda x : (memoria.index(x),x),memoria))
    vacios_filtrados = list(filter(lambda y : type(y[1][1])==Vacio and int(y[1][1].memoria)>=tamanyo,lista_position))
    if(len(vacios_filtrados)!=0):
        hueco = vacios_filtrados[0]
        for vacio in vacios_filtrados:
            if(int(hueco[1][1].memoria)>int(vacio[1][1].memoria)):
                hueco = vacio
    return hueco

def addProcesos(lista): #comprobar de no pasar listas vacias
    sobras = []
    if(len(memoria)==0):
      sobras = siMemoriaVacia(lista) 
    else:
        for proceso in lista:
            tamanyo = int(proceso.memoria)
            hueco = mejorHueco(tamanyo)
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


def cadenaAEscribir(iteracion):
    cadena = str(iteracion) + " "
    for particion in memoria:
        cadena += "[" + str(particion[0]) 
        cadena += " " + particion[1].nombre
        cadena += " " + str(particion[1].memoria) + "] "
    cadena += "\n"
    
    return cadena

def ejecutar():#cambiar tiene que seguir hasta que se quede vacio
    sobras = []
    count = 0
    while count<int(lista_procesos[len(lista_procesos)-1].llegada):
        count+=1
        lista_proc = list(filter(lambda x : int(x.llegada)==count , lista_procesos))
        for sobra in sobras :
            lista_proc.append(sobra)
        lista_proc = sorted(lista_proc,key=lambda p : p.llegada)


        for proceso in memoria:
            pasaTiempo(proceso[1])
    

        limpiarmemoria()
    
        sobras = addProcesos(lista_proc)
        escribir("particiones.txt",cadenaAEscribir(count))
ejecutar()
    