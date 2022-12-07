class Particion:
    def __init__(self,nombre,llegada,memoria:int,Tejecucion):
        self.nombre = nombre
        self.llegada = llegada
        self.memoria = memoria
        self.Tejecucion = Tejecucion

    def restarTiempo(self):
        self.Tejecucion=int(self.Tejecucion)-1
    

    def toString(self):
        return "progreso = " + self.nombre + "," + self.llegada + "," + self.memoria + "," + self.Tejecucion

    def haTeminado(self):
        if(int(self.Tejecucion) == 0):
            return True
        else:
            return False