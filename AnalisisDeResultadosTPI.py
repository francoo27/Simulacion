import numpy as np
from enum import Enum

class DATA_TYPE(Enum):
    INT = "INT"
    FLOAT = "FLOAT"

class Iteracion():
    def __init__(self,
                numIteracion,
                cantidadProductos,
                cantidadServicios,
                colaturnoLongitud,
                colaATMLongitud,
                colaVentanillaLongitud,
                colaCubiculoLongitud,
                colaSelectLongitud,
                ATM1Utilizacion,
                ATM2Utilizacion,
                ATM3Utilizacion,
                ATM4Utilizacion,
                cantidadGenteQueTermino,
                cantidadRetroalimentacion,
                colaTurnoTimeout,
                colaATMTimeout,
                colaVentanillaTimeout,
                colaCubiculosTimeout,
                colaSelectTimeout):
        self.numIteracion = numIteracion 
        self.cantidadProductos = cantidadProductos 
        self.cantidadServicios = cantidadServicios 
        self.colaturnoLongitud = colaturnoLongitud 
        self.colaATMLongitud = colaATMLongitud 
        self.colaVentanillaLongitud = colaVentanillaLongitud 
        self.colaCubiculoLongitud = colaCubiculoLongitud 
        self.colaSelectLongitud = colaSelectLongitud 
        self.ATM1Utilizacion = ATM1Utilizacion 
        self.ATM2Utilizacion = ATM2Utilizacion 
        self.ATM3Utilizacion = ATM3Utilizacion 
        self.ATM4Utilizacion = ATM4Utilizacion 
        self.cantidadGenteQueTermino = cantidadGenteQueTermino 
        self.cantidadRetroalimentacion = cantidadRetroalimentacion 
        self.colaTurnoTimeout = colaTurnoTimeout 
        self.colaATMTimeout = colaATMTimeout 
        self.colaVentanillaTimeout = colaVentanillaTimeout 
        self.colaCubiculosTimeout = colaCubiculosTimeout 
        self.colaSelectTimeout = colaSelectTimeout 

def getMeanOfArray(arr,dataType):
    if dataType.value == DATA_TYPE.INT.value:
        acum = 0
    if dataType.value == DATA_TYPE.FLOAT.value:
        acum = 0.0
    for val in arr:
        acum += val
    return acum / len(arr)


iteraciones = []
aux = []
file1 = open("Iteraciones.txt","r") 
filestring = file1.read()
file1.close()

rows = filestring.split(";")
rowSplit = []
counter = 0
for row in rows:
    rowSplit = row.split(",")
    if counter <= 99:
        iteracion = Iteracion(rowSplit[0],rowSplit[1],rowSplit[2],rowSplit[3],rowSplit[4],rowSplit[5],
                            rowSplit[6],rowSplit[7],rowSplit[8],rowSplit[9],rowSplit[10],rowSplit[11],
                            rowSplit[12],rowSplit[13],rowSplit[14],rowSplit[15],rowSplit[16],rowSplit[17],rowSplit[18])
        iteraciones.append(iteracion)
        counter+=1
    rowSplit = []
ATM1Utilizaciones = []
for iteracion in iteraciones:
    ATM1Utilizaciones.append(float(iteracion.ATM1Utilizacion))

ATM1UtilizacionesMEAN = getMeanOfArray(ATM1Utilizaciones,DATA_TYPE.FLOAT)
print(ATM1Utilizaciones)
print(ATM1UtilizacionesMEAN)