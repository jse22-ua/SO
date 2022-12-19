#Clase que guardará el proceso con sus nombre, tiempo de llegada
# memoria y tiempo de ejecución 
class Particion:
    def __init__(self,nombre,llegada,memoria:int,Tejecucion):
        self.nombre = nombre
        self.llegada = llegada
        self.memoria = memoria
        self.Tejecucion = Tejecucion

    #resta el tiempo de ejecucion
    def restarTiempo(self):
        self.Tejecucion=int(self.Tejecucion)-1
    
    #metodo para realizar pruebas
    #devuelve un string con las caracteristica del proceso
    def toString(self):
        return "progreso = " + self.nombre + "," + str(self.llegada) + "," + str(self.memoria) + "," + str(self.Tejecucion)
