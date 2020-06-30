from tkinter import *
# from tkinter.ttk import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib import style
from matplotlib import animation
style.use("ggplot")
LARGE_FONT = ("Verdana",12)
from random import randint

import plotly.express as px
import plotly.graph_objects as go
from matplotlib import pyplot as plt
from enum import Enum
from pprint import pprint
import numpy as np

class SERVER_STATUS(Enum):
    DISPONIBLE = 0
    OCUPADO = 1

class EVENT_TYPE(Enum):
    ARRRIBO = "A"
    PARTIDA = "P"
    UNKNOWN = ""

# Sitema MM1
class Sim:
    def __init__(self,codigo,serverEstatus,
                nextEvent,clock,
                totalDelay,timeServiceacumulated,
                areaQ,areaB,
                timeOfLastEvent,numberOfClientsInQueue,
                numberOfClientsCompletedWithDelay,
                number,
                midTimeArrivals,
                midTimeService): 
        self.codigo=codigo or 0
        self.serverEstatus = serverEstatus or SERVER_STATUS.DISPONIBLE.value
        self.nextEvent = nextEvent or ""
        self.clock = clock or 0.0
        self.totalDelay = totalDelay or 0.0
        self.timeServiceacumulated = timeServiceacumulated or 0.0
        self.areaQ = areaQ or 0.0
        self.areaB = areaB or 0.0
        self.timeOfLastEvent = timeOfLastEvent or 0.0 
        self.numberOfClientsInQueue = numberOfClientsInQueue or 0
        self.numberOfClientsCompletedWithDelay = numberOfClientsCompletedWithDelay or 0.0
        self.midTimeArrivals = midTimeArrivals or 0.0
        self.midTimeService = midTimeService or 0.0
        self.eventList = []
        self.queue = []
        #Listas para generar las gráficas
        self.clientQueueinT = []
        self.clockinT = []
        self.tsAcuminT = []
        #Tiempo del primer arribo
        self.eventList.append(np.random.exponential(1/self.midTimeArrivals))
        self.simulationEnded = False
        #Le pongo un número grande para asegurarme que el primer evento sea un arribo
        self.eventList.append(number)

    def getTimeEvent(self):
        self.timeOfLastEvent = self.clock
        if self.eventList[0] <= self.eventList[1]:
            self.clock = self.eventList[0]
            self.nextEvent = EVENT_TYPE.ARRRIBO.value
        else:
            self.clock = self.eventList[1]
            self.nextEvent = EVENT_TYPE.PARTIDA.value

    def arrival(self):
        #Todo arribo desencadena un nuevo arribo
        self.eventList[0] = self.clock + np.random.exponential(1/self.midTimeArrivals)
        #Pregunto si el servidor está disponible
        if self.serverEstatus == SERVER_STATUS.DISPONIBLE.value:

            # Cambio el servidor al estado Ocupado
            self.serverEstatus = SERVER_STATUS.OCUPADO.value

            # Programo el próximo evento partida
            self.eventList[1] = self.clock + np.random.exponential(1/self.midTimeService)
            
            #Acumulo el tiempo de servicio
            self.timeServiceacumulated += (self.eventList[1] - self.clock)

            #Actualizo la cantidad de clientes que completaron la demora
            self.numberOfClientsCompletedWithDelay += 1

            #-----------Gráficas---------------
            self.clockinT.append(self.clock)
            self.clientQueueinT.append(self.numberOfClientsInQueue)
            self.tsAcuminT.append(self.timeServiceacumulated)
            
        else:
            #Calculo área bajo Q(t) desde el momento actual del reloj hacia atrás (tiempo del último evento)
            self.areaQ += (self.numberOfClientsInQueue * (self.clock - self.timeOfLastEvent))     

            #Incremento la cantidad de clientes en cola en 1       
            self.numberOfClientsInQueue +=1

            #Guardo el valor del reloj en la posición "Nro de Clientes en cola" para saber
            #cuando llegó el cliente a la cola y más adelante calcular la demora
            self.queue.append(self.clock)

            #--------- Gráficas---------------------
            self.clockinT.append(self.clock)
            self.clientQueueinT.append(self.numberOfClientsInQueue)
            self.tsAcuminT.append(self.timeServiceacumulated)            

    
    def departure(self):          
        #Pregunto si hay clientes en cola 
        if self.numberOfClientsInQueue > 0:
            #Tiempo del próximo evento partida
            self.eventList[1] = self.clock + np.random.exponential(1/self.midTimeService)
            #Acumulo la la demora acumulada como el valor actual del reloj menos el valor del
            # reloj cuando el cliente ingresó a la cola
            self.totalDelay += self.clock - self.queue[0]

            #Actualizo el contador de clientes que completaron demora
            self.numberOfClientsCompletedWithDelay += 1

            #Acumulo el tiempo de servicio
            self.timeServiceacumulated += (self.eventList[1] - self.clock)

            #Calculo el área bajo Q(t) del período anterior (Reloj - Tiempo del último evento)
            self.areaQ += (self.numberOfClientsInQueue * (self.clock - self.timeOfLastEvent))

            #Decremento la cantidad de clientes en cola en uno
            self.numberOfClientsInQueue -= 1

            #Voy a desplazar a los valores de la cola un lugar hacia arriba
            self.queue.pop(0)

            #----------- Gráfcias ----------------
            self.clockinT.append(self.clock)
            self.clientQueueinT.append(self.numberOfClientsInQueue)
            self.tsAcuminT.append(self.timeServiceacumulated)
           
        else:
            #Si no hay clientes en la cola, establezco el estado del servidor en "Disponible"
            self.serverEstatus = SERVER_STATUS.DISPONIBLE.value

            #Forzar a que no haya partidas si no hay clientes atendiendo
            self.eventList[1] = 99999999

            #----------- Gráficas ----------------
            self.clockinT.append(self.clock)
            self.clientQueueinT.append(self.numberOfClientsInQueue)
            self.tsAcuminT.append(self.timeServiceacumulated)
    
    #Número promedio de clientes en cola
    def getMeanOfClientsInQueue(self):
        if self.clock !=0:
            average_num_of_queued_costumers = self.areaQ/self.clock
            return average_num_of_queued_costumers
        else:
            average_num_of_queued_costumers = 0
            return average_num_of_queued_costumers
        
    
    # Utilización promedio del servidor
    def getMeanOfServerUtilization(self):
        if self.clock != 0:
            average_server_utilization = self.timeServiceacumulated/self.clock
            return average_server_utilization
        else:
            average_server_utilization = 0
            return average_server_utilization      
        
    # Demora promedio de los clientes
    def getAverageCustomerDelay(self):
        if self.numberOfClientsCompletedWithDelay != 0:
            average_costumers_delay = self.totalDelay/self.numberOfClientsCompletedWithDelay
            return average_costumers_delay
        else:
            average_costumers_delay = 0
            return average_costumers_delay


def getArrayFilledWithSecuencialNumbers(maxValue):
    arr = [0] * ( maxValue + 1 )
    i = 0
    while i <= maxValue:
        arr[i] = i
        i+=1
    return arr 


def getCount(arr):
    arr.sort()
    counter = [0] * ( arr[-1] + 1 )
    for e in arr:
        counter[e] += 1
    return counter


def plotNumberOfClientsInQueue(clientQueueinT):
    ## input clientQueueinT of instance of simulation
    plt.xticks(getArrayFilledWithSecuencialNumbers(max(clientQueueinT)))
    plt.bar(getArrayFilledWithSecuencialNumbers(max(clientQueueinT)),getCount(clientQueueinT))
    plt.show()


def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("No es un entero , porfavor ingrese nuevamente")
       continue
    else:
       return userInput 
       break      

def plotClientsInQueue(simulation):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=simulation.clockinT, y=simulation.clientQueueinT,
                mode='lines',
                name='lines'))
    fig.show()

def plotBoxClientsInQueue(simulation):
        fig = go.Figure()
        fig.add_trace(go.Box(
            y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,3,3,5,4,4,6,6,8,8,9,9,7,7,10,10,11,11,19,23,21,22],
            name="All Points",
            jitter=0.3,
            pointpos=-1.8,
            boxpoints='all', # represent all points
            marker_color='rgb(7,40,89)',
            line_color='rgb(7,40,89)'
        ))
        fig.show()

def plotServerPerformance(tsAcuminT, clockinT):
    uti = []
    for i in range(len(clockinT)):
        uti.append(tsAcuminT[i]/clockinT[i])
    plt.title('Utilización del servidor')
    plt.plot(clockinT,uti)
    plt.ylabel('Utilización del servidor')
    plt.xlabel('tiempo')
    plt.show()

def main(simulacion):
        simulacion.getTimeEvent()
        if simulacion.nextEvent == EVENT_TYPE.ARRRIBO.value:
            simulacion.arrival()
        else:
            simulacion.departure()
        # if (simulacion.clock > 500):
        #     simulacion.simulationEnded = True
        #     break



###GUI STUFF
def animate(i):
    global simulacion
    if (not simStopped):
        main(simulacion)
        xList.append(simulacion.clock)
        yList.append(len(simulacion.queue))
        yList2.append(simulacion.timeServiceacumulated)
        a.clear()
        a.plot(xList,yList)
        b.clear()
        b.plot(xList,yList2,color= 'b')
        a.axhline(y=simulacion.getMeanOfClientsInQueue(), color="black", linestyle=":")
        b.axhline(y=simulacion.getMeanOfServerUtilization(), color="black", linestyle=":")

def changeSimState(button):
    global simStopped
    if(simStopped):
        button['text'] = "Parar"
        simStopped = False
    else:
        button['text'] = "Iniciar"
        simStopped = True
def restartSimulation():
    global a
    global b
    global simulacion 
    simulacion = Sim(0,SERVER_STATUS.DISPONIBLE.value,EVENT_TYPE.UNKNOWN.value,0.0,0.0,0.0,0.0,0.0,0.0,0,0,99999999,7.0,9.0)
    a.clear()
    b.clear()
    yList.clear()
    xList.clear()
    yList2.clear()

def changeScale(value):
    simulacion.midTimeArrivals = float(value)
    print(simulacion.midTimeArrivals)
### GUI VARS
simStopped = True

root = tk.Tk()
figure = Figure(figsize=(5, 4), dpi=100)
a = figure.add_subplot(111)

figure2 = Figure(figsize=(5, 4), dpi=100)
b = figure2.add_subplot(111)

xList = []
yList = []
yList2 = []
### GUI VARS


simulacion = Sim(0,SERVER_STATUS.DISPONIBLE.value,EVENT_TYPE.UNKNOWN.value,0.0,0.0,0.0,0.0,0.0,0.0,0,0,99999999,7.0,9.0)



#estrutcura gui
# --------
# tl|tc|tr
# --------
# --|mc|--
# --------
# bl|bc|br
# --------


leftFrame = Frame(root)
leftFrame.pack( side = tk.LEFT )

centerFrame = Frame(root)
centerFrame.pack( side = tk.LEFT )

rightFrame = Frame(root)
rightFrame.pack( side = tk.LEFT )

topLeftFrame = Frame(leftFrame)
topLeftFrame.pack(side=tk.TOP)

bottomLeftFrame = Frame(leftFrame)
bottomLeftFrame.pack(side=tk.BOTTOM)


RestartSimulatioButton = tk.Button(centerFrame, text ="Reiniciar", command = restartSimulation)
RestartSimulatioButton.pack()
StateSimulationButton = tk.Button(centerFrame, text ="Iniciar", command = lambda: changeSimState(StateSimulationButton))
StateSimulationButton.pack()


Scalevar = DoubleVar().set(0.5)
Scale = Scale( centerFrame, variable = Scalevar ,from_ = 0.1 , to = 0.98, digits = 3, resolution = 0.01,command =changeScale)
Scale.pack(anchor="n")



canvas = FigureCanvasTkAgg(figure, topLeftFrame)
toolbar = NavigationToolbar2Tk(canvas, topLeftFrame)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas2 = FigureCanvasTkAgg(figure2, bottomLeftFrame)
toolbar2 = NavigationToolbar2Tk(canvas2, bottomLeftFrame)
toolbar2.update()
canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

ani = animation.FuncAnimation(figure, animate,interval=200)
ani2 = animation.FuncAnimation(figure2, animate,interval=200)
root.mainloop()
