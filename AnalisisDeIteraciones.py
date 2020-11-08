import numpy as np
import math as mt
import statistics 
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
iteraciones2 = []
aux = []
file1 = open("Iteraciones.txt","r") 
filestring = file1.read()
file1.close()

file2 = open("IteracionesB.txt","r") 
filestring2 = file2.read()
file2.close()

rows = filestring.split(";")
rows2 = filestring2.split(";")
rowSplit = []
rowSplit2 = []
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

counter = 0
totalRows=len(rows2)-1
for row in rows2:
    rowSplit2 = row.split(",")
    if counter < totalRows:
        iteracion2 = Iteracion(rowSplit2[0],rowSplit2[1],rowSplit2[2],rowSplit2[3],rowSplit2[4],rowSplit2[5],
                            rowSplit2[6],rowSplit2[7],rowSplit2[8],rowSplit2[9],rowSplit2[10],rowSplit2[11],
                            rowSplit2[12],rowSplit2[13],rowSplit2[14],rowSplit2[15],rowSplit2[16],rowSplit2[17],rowSplit2[18])
        iteraciones2.append(iteracion2)
        counter+=1
    rowSplit = []

meanArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# varArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# stdArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# count= 0
# while count < totalRows:
#     meanArray[0]+=float((float)(iteraciones[count].cantidadProductos) - (float)(iteraciones2[count].cantidadProductos))/totalRows
#     meanArray[1]+=float((float)(iteraciones[count].cantidadServicios) - (float)(iteraciones2[count].cantidadServicios ))/totalRows
#     meanArray[2]+=float((float)(iteraciones[count].colaturnoLongitud) - (float)(iteraciones2[count].colaturnoLongitud))/totalRows
#     meanArray[3]+=float((float)(iteraciones[count].colaATMLongitud) - (float)(iteraciones2[count].colaATMLongitud))/totalRows
#     meanArray[4]+=float((float)(iteraciones[count].colaVentanillaLongitud) - (float)(iteraciones2[count].colaVentanillaLongitud))/totalRows
#     meanArray[5]+=float((float)(iteraciones[count].colaCubiculoLongitud) - (float)(iteraciones2[count].colaCubiculoLongitud))/totalRows
#     meanArray[6]+=float((float)(iteraciones[count].colaSelectLongitud) - (float)(iteraciones2[count].colaSelectLongitud))/totalRows
#     meanArray[7]+=float((float)(iteraciones[count].ATM1Utilizacion) - (float)(iteraciones2[count].ATM1Utilizacion))/totalRows
#     meanArray[8]+=float((float)(iteraciones[count].ATM2Utilizacion) - (float)(iteraciones2[count].ATM2Utilizacion))/totalRows
#     meanArray[9]+=float((float)(iteraciones[count].ATM3Utilizacion) - (float)(iteraciones2[count].ATM3Utilizacion))/totalRows
#     meanArray[10]+=float((float)(iteraciones[count].ATM4Utilizacion) - (float)(iteraciones2[count].ATM4Utilizacion))/totalRows
#     meanArray[11]+=float((float)(iteraciones[count].cantidadGenteQueTermino) - (float)(iteraciones2[count].cantidadGenteQueTermino))/totalRows
#     meanArray[12]+=float((float)(iteraciones[count].cantidadRetroalimentacion) - (float)(iteraciones2[count].cantidadRetroalimentacion))/totalRows
#     meanArray[13]+=float((float)(iteraciones[count].colaTurnoTimeout) - (float)(iteraciones2[count].colaTurnoTimeout))/totalRows
#     meanArray[14]+=float((float)(iteraciones[count].colaATMTimeout) - (float)(iteraciones2[count].colaATMTimeout))/totalRows
#     meanArray[15]+=float((float)(iteraciones[count].colaVentanillaTimeout) - (float)(iteraciones2[count].colaVentanillaTimeout))/totalRows
#     meanArray[16]+=float((float)(iteraciones[count].colaCubiculosTimeout)- (float)(iteraciones2[count].colaCubiculosTimeout))/totalRows
#     meanArray[17]+=float((float)(iteraciones[count].colaSelectTimeout) - (float)(iteraciones2[count].colaSelectTimeout))/totalRows
#     count+=1



# # Calculo de Zj
# Zj = []
# count = 0 
# while count < totalRows:
#     Zj = float((float)(iteraciones[count].cantidadProductos) - (float)(iteraciones2[count].cantidadProductos))

# # Calculo de Zn

# Zn = Zj / 100








counta = 0
t = 1.660
meanArrayToCalculate = [ [0]*totalRows for i in range(18)]
meanArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
varArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
intervalArrayResults = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while counta < totalRows:
    meanArrayToCalculate[0][counta]=float((float)(iteraciones[counta].cantidadProductos) - (float)(iteraciones2[counta].cantidadProductos))
    meanArrayToCalculate[1][counta]=float((float)(iteraciones[counta].cantidadServicios) - (float)(iteraciones2[counta].cantidadServicios ))
    meanArrayToCalculate[2][counta]=float((float)(iteraciones[counta].colaturnoLongitud) - (float)(iteraciones2[counta].colaturnoLongitud))
    meanArrayToCalculate[3][counta]=float((float)(iteraciones[counta].colaATMLongitud) - (float)(iteraciones2[counta].colaATMLongitud))
    meanArrayToCalculate[4][counta]=float((float)(iteraciones[counta].colaVentanillaLongitud) - (float)(iteraciones2[counta].colaVentanillaLongitud))
    meanArrayToCalculate[5][counta]=float((float)(iteraciones[counta].colaCubiculoLongitud) - (float)(iteraciones2[counta].colaCubiculoLongitud))
    meanArrayToCalculate[6][counta]=float((float)(iteraciones[counta].colaSelectLongitud) - (float)(iteraciones2[counta].colaSelectLongitud))
    meanArrayToCalculate[7][counta]=float((float)(iteraciones[counta].ATM1Utilizacion) - (float)(iteraciones2[counta].ATM1Utilizacion))
    meanArrayToCalculate[8][counta]=float((float)(iteraciones[counta].ATM2Utilizacion) - (float)(iteraciones2[counta].ATM2Utilizacion))
    meanArrayToCalculate[9][counta]=float((float)(iteraciones[counta].ATM3Utilizacion) - (float)(iteraciones2[counta].ATM3Utilizacion))
    meanArrayToCalculate[10][counta]=float((float)(iteraciones[counta].ATM4Utilizacion) - (float)(iteraciones2[counta].ATM4Utilizacion))
    meanArrayToCalculate[11][counta]=float((float)(iteraciones[counta].cantidadGenteQueTermino) - (float)(iteraciones2[counta].cantidadGenteQueTermino))
    meanArrayToCalculate[12][counta]=float((float)(iteraciones[counta].cantidadRetroalimentacion) - (float)(iteraciones2[counta].cantidadRetroalimentacion))
    meanArrayToCalculate[13][counta]=float((float)(iteraciones[counta].colaTurnoTimeout) - (float)(iteraciones2[counta].colaTurnoTimeout))
    meanArrayToCalculate[14][counta]=float((float)(iteraciones[counta].colaATMTimeout) - (float)(iteraciones2[counta].colaATMTimeout))
    meanArrayToCalculate[15][counta]=float((float)(iteraciones[counta].colaVentanillaTimeout) - (float)(iteraciones2[counta].colaVentanillaTimeout))
    meanArrayToCalculate[16][counta]=float((float)(iteraciones[counta].colaCubiculosTimeout)- (float)(iteraciones2[counta].colaCubiculosTimeout))
    meanArrayToCalculate[17][counta]=float((float)(iteraciones[counta].colaSelectTimeout) - (float)(iteraciones2[counta].colaSelectTimeout))

    counta+=1
acum = 0
# for n in meanArraye[0]:
#     acum+=n    
# acum = acum / 100
# print(acum)

# acum = (float)(statistics.mean(meanArrayToCalculate[0]))
i=0
file1 = open("IteracionesResultadoProcesado.txt","w+") 
while i <= 17:
    meanArrayResults[i] = (float)(statistics.mean(meanArrayToCalculate[i]))
    for n in meanArrayToCalculate[i]:
        varArrayResults[i] += mt.pow((n - meanArrayResults[i]),2)
    varArrayResults[i] = varArrayResults[i]/(totalRows*(totalRows-1))
    intervalArrayResults[i] = mt.sqrt(varArrayResults[i])
    print("Z[N]:",meanArrayResults[i]," +- ",intervalArrayResults[i])
    print("Z[N]:",meanArrayResults[i]," +- ",intervalArrayResults[i],file=file1)
    i+=1


file1.close()


