# TAXI - MATRICULACIÓN // PYTHON & MYSQL

Se pretende crear una tabla en MySQL con los campos de las matriculas, marcas de coche, fecha y eurotaxi e insertar los respectivos datos a dichos campos, datos que se pueden obtener del archivo "TAXI_Flota_Diario.csv" publicada en la web del ayuntamiento de Madrid.

Para ello, previamente, creamos una clase en Python de forma que nos facilite y nos resulte mas cómodo y legible la manipulación de los datos del archivo .csv

```python
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
# Se puede observar que hay ciertas columnas que en teoria el valor deberia ser un entero (Int), y sin embargo hay un espacio nulo o algun caracter, esto es debido por la mala creacion del csv. Así se desea implementar varios metodos que "limpien" estos campos, de forma que si es un valor no entero lo sustituya por un 0
def limpiarToInt(lista):
    for i in range(len(lista)):
        try:
            lista[i]=int(lista[i])
        except:
            lista[i]=0
    return lista
# Analogo si se desea que sea un valor flotante y 0.0 respectivamente.
def limpiarToFloat(lista):
    for i in range(len(lista)):
        try:
            lista[i]=float(lista[i])
        except:
            lista[i]=0.0
    return lista
```

Así, mediante la clase ya creada y subida en un antiguo repositorio: [Clase DataBase - Python & MySQL](https://github.com/rafafrdz/ClassDataBase-PythonMySQL) (Clase que creamos para facilitarnos el uso de MySQL mediante Python)

El propósito del ejercicio queda resuelto de la siguiente forma:

```python
from Curso.database.ClassDB import DataBase
from Curso.database.ClassTaxis import Taxis

taxidb = DataBase('localhost',3310,'root','root',"taxi")
taxidb.openDB()

#-- Crear la tabla matriculacion con las columnas
taxidb.crearTabla('matriculacion','matriculas','fecha','marca','eurotaxi')

# -- Tomar los datos del archivo
taxiCsv = Taxis("TAXI_Flota_Diario.csv")
matriculas, fecha, marca, eurotaxi = taxiCsv.matriculas(), taxiCsv.columna(2), taxiCsv.marcas(), taxiCsv.columna(13)

# -- Insertar datos (tomamos como ejemplo insertar 10 valores, sino tardaria mucho)
for i in range(10):
    taxidb.insert('matriculacion',i,matriculas[i],fecha[i],marca[i],eurotaxi[i])

taxidb.closeDB()
```

