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
