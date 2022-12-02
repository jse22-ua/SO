class Particion:
    def __init__(self,nombre,llegada,memoria,Tejecucion):
        self.nombre = nombre
        self.llegada = llegada
        self.memoria = memoria
        self.Tejecucion = Tejecucion

    def restarTiempo(self):
        self.Tejecucion=self.Tejecucion-1
    

    def toString(self):
        return "progreso = " + self.nombre + "," + self.llegada + "," + self.memoria + "," + self.Tejecucion
