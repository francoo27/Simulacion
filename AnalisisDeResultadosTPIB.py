import numpy as np
import math as mt
from prettytable import PrettyTable
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

def getMeanOfArray(arr):
    acum = 0
    for val in arr:
        acum += val
    return acum / len(arr)


iteraciones = []
aux = []
file1 = open("IteracionesB.txt","r") 
filestring = file1.read()
file1.close()

rows = filestring.split(";")
rowSplit = []
counter = 0
totalRows=len(rows)-1
for row in rows:
    rowSplit = row.split(",")
    if counter < totalRows:
        iteracion = Iteracion(rowSplit[0],rowSplit[1],rowSplit[2],rowSplit[3],rowSplit[4],rowSplit[5],
                            rowSplit[6],rowSplit[7],rowSplit[8],rowSplit[9],rowSplit[10],rowSplit[11],
                            rowSplit[12],rowSplit[13],rowSplit[14],rowSplit[15],rowSplit[16],rowSplit[17],rowSplit[18])
        iteraciones.append(iteracion)
        counter+=1
    rowSplit = []

x = PrettyTable()

meanArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
varArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stdArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
intervalArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
meanArray = [ [0]*totalRows for i in range(18)]
counter = 0
for iteracion in iteraciones:
    if counter < totalRows:
        meanArray[0][counter]=int(iteracion.cantidadProductos)
        meanArray[1][counter]=int(iteracion.cantidadServicios)
        meanArray[2][counter]=float(iteracion.colaturnoLongitud)
        meanArray[3][counter]=float(iteracion.colaATMLongitud)
        meanArray[4][counter]=float(iteracion.colaVentanillaLongitud)
        meanArray[5][counter]=float(iteracion.colaCubiculoLongitud)
        meanArray[6][counter]=float(iteracion.colaSelectLongitud)
        meanArray[7][counter]=float(iteracion.ATM1Utilizacion)
        meanArray[8][counter]=float(iteracion.ATM2Utilizacion)
        meanArray[9][counter]=float(iteracion.ATM3Utilizacion)
        meanArray[10][counter]=float(iteracion.ATM4Utilizacion)
        meanArray[11][counter]=int(iteracion.cantidadGenteQueTermino)
        meanArray[12][counter]=int(iteracion.cantidadRetroalimentacion)
        meanArray[13][counter]=int(iteracion.colaTurnoTimeout)
        meanArray[14][counter]=int(iteracion.colaATMTimeout)
        meanArray[15][counter]=int(iteracion.colaVentanillaTimeout)
        meanArray[16][counter]=int(iteracion.colaCubiculosTimeout)       
        meanArray[17][counter]=int(iteracion.colaSelectTimeout)         

    counter+=1

counter = 0
while counter <= 17:
    meanArrayResults[counter] = getMeanOfArray(meanArray[counter])
    varArrayResults[counter] = np.var(meanArray[counter])
    stdArrayResults[counter] = np.std(meanArray[counter])
    intervalArrayResults[counter] = 1.833 * (mt.sqrt(varArrayResults[counter]/totalRows))
    counter+=1
    
x.field_names = ["Medida", "Media", "Varianza", "Desviacion estandar","Intervalo de confianza"]
x.add_row(["cantidadProductos",meanArrayResults[0], varArrayResults[0], stdArrayResults[0], intervalArrayResults[0]])
x.add_row(["cantidadServicios",meanArrayResults[1], varArrayResults[1], stdArrayResults[1], intervalArrayResults[1]])
x.add_row(["colaturnoLongitud",meanArrayResults[2], varArrayResults[2], stdArrayResults[2], intervalArrayResults[2]])
x.add_row(["colaATMLongitud",meanArrayResults[3], varArrayResults[3], stdArrayResults[3], intervalArrayResults[3]])
x.add_row(["colaVentanillaLongitud",meanArrayResults[4], varArrayResults[4], stdArrayResults[4], intervalArrayResults[4]])
x.add_row(["colaCubiculoLongitud",meanArrayResults[5], varArrayResults[5], stdArrayResults[5], intervalArrayResults[5]])
x.add_row(["colaSelectLongitud",meanArrayResults[6], varArrayResults[6], stdArrayResults[6], intervalArrayResults[6]])
x.add_row(["ATM1Utilizacion",meanArrayResults[7], varArrayResults[7], stdArrayResults[7], intervalArrayResults[7]])
x.add_row(["ATM2Utilizacion",meanArrayResults[8], varArrayResults[8], stdArrayResults[8], intervalArrayResults[8]])
x.add_row(["ATM3Utilizacion",meanArrayResults[9], varArrayResults[9], stdArrayResults[9], intervalArrayResults[9]])
x.add_row(["ATM4Utilizacion",meanArrayResults[10], varArrayResults[10], stdArrayResults[10], intervalArrayResults[10]])
x.add_row(["cantidadGenteQueTermino",meanArrayResults[11], varArrayResults[11], stdArrayResults[11], intervalArrayResults[11]])
x.add_row(["cantidadRetroalimentacion",meanArrayResults[12], varArrayResults[12], stdArrayResults[12], intervalArrayResults[12]])
x.add_row(["colaTurnoTimeout",meanArrayResults[13], varArrayResults[13], stdArrayResults[13], intervalArrayResults[13]])
x.add_row(["colaATMTimeout",meanArrayResults[14], varArrayResults[14], stdArrayResults[14], intervalArrayResults[14]])
x.add_row(["colaVentanillaTimeout",meanArrayResults[15], varArrayResults[15], stdArrayResults[15], intervalArrayResults[15]])
x.add_row(["colaCubiculosTimeout",meanArrayResults[16], varArrayResults[16], stdArrayResults[16], intervalArrayResults[16]])
x.add_row(["colaSelectTimeout",meanArrayResults[17], varArrayResults[17], stdArrayResults[17], intervalArrayResults[17]])
print(x)
