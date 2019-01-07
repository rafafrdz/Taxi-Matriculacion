class Taxis(object):
    def __init__(self,rutaArchivo):
        self.rutaArchivo = rutaArchivo
    def __leerArchivo(self,colum):
        f = open(self.rutaArchivo, 'r')
        marca = []
        while True:
            linea = f.readline()
            if not linea:
                break
            linea = linea.split(';')
            marca.append(linea[colum])
        return marca[1:]
    def columna(self,colum):
        return self.__leerArchivo(colum)
    def marcas(self):
        return self.columna(3)
    def codigos(self):
        return list(map(lambda x:int(x),self.columna(0)))
    def matriculas(self):
        return self.columna(1)
    def plazas(self):
        return self.columna(11)
        
# Se puede observar que hay ciertas columnas que en teoria el valor
# deberia ser un entero (Int), y sin embargo hay un espacio nulo o
# algun caracter, esto es debido por la mala creacion del csv.
# Así se desea implementar varios metodos que "limpien" estos campos,
# de forma que si es un valor no entero lo sustituya por un 0

def limpiarToInt(lista):
    for i in range(len(lista)):
        try:
            lista[i]=int(lista[i])
        except:
            lista[i]=0
    return lista
def limpiarToFloat(lista):
    for i in range(len(lista)):
        try:
            lista[i]=float(lista[i])
        except:
            lista[i]=0.0
    return lista
