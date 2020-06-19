import numpy as np
from matplotlib import pyplot as plt
from enum import Enum
from pprint import pprint


simulaciones = []

class SERVER_STATUS(Enum):
    DISPONIBLE = 0
    OCUPADO = 1

class EVENT_TYPE(Enum):
    ARRRIBO = "A"
    PARTIDA = "P"
    UNKNOWN = ""

# Sitema MM1
class Sim:
    id=0
    nextEvent = "" # A - Arribo | P - Partida
    serverEstatus = 0 # 1 - Diponible | 0 - Ocupado
    numberOfClientsInQueue = 0
    timeServiceacumulated = 0.0
    clock = 0.0
    midTimeArrivals = 0.0
    midTimeService = 0.0
    numberOfClientsCompletedWithDelay = 0
    timeOfLastEvent = 0.0
    eventList = []
    queue = []
    totalDelay = 0.0
    areaQ = 0.0
    areaB = 0.0
    #Listas para generar las gráficas
    clientQueueinT = []
    clockinT = []
    tsAcuminT = []
    def __init__(self,id,serverEstatus,
                nextEvent,clock,
                totalDelay,timeServiceacumulated,
                areaQ,areaB,
                timeOfLastEvent,numberOfClientsInQueue,
                numberOfClientsCompletedWithDelay,
                number,
                midTimeArrivals,
                midTimeService): 
        self.id=id
        self.serverEstatus = serverEstatus
        self.nextEvent = nextEvent
        self.clock = clock
        self.totalDelay = totalDelay
        self.timeServiceacumulated = timeServiceacumulated
        self.areaQ = areaQ
        self.areaB = areaB
        self.timeOfLastEvent = timeOfLastEvent
        self.numberOfClientsInQueue = numberOfClientsInQueue
        self.numberOfClientsCompletedWithDelay = numberOfClientsCompletedWithDelay
        self.midTimeArrivals = midTimeArrivals
        self.midTimeService = midTimeService

        #Tiempo del primer arribo
        self.eventList.append(np.random.exponential(1/self.midTimeArrivals))

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
            ####### A ESTE ELSE NO ENTRA NUNCA #######

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

        ####### A LA PRIMERA PARTE DEL IF NO ENTRA NUNCA #######
        if self.numberOfClientsInQueue > 0:
            #Tiempo del próximo evento partida
            self.eventList[1] = self.clock + np.random.exponential(1/self.midTimeArrivals)
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
        
    
def main(simulacion):
    while ((simulacion.clock <= 10000) or (simulacion.numberOfClientsInQueue != 0) or (simulacion.serverEstatus != SERVER_STATUS.DISPONIBLE.value)):
        simulacion.getTimeEvent()
        if simulacion.nextEvent == EVENT_TYPE.ARRRIBO.value:
            simulacion.arrival()
        else:
            simulacion.departure()

    #     pprint(vars(simulacion))
    #     print("eventList",simulacion.eventList)
    #     print("queue",simulacion.queue)
    #     print("clientQueueinT",simulacion.clientQueueinT)
    #     print("clockinT",simulacion.clockinT)
    #     print("tsAcuminT",simulacion.tsAcuminT)
    # print('Cantidad promedio de clientes en cola:', simulacion.getMeanOfClientsInQueue())
    # print('Promedio de utilizacion del servidor:', simulacion.getMeanOfServerUtilization())        
    # print('Tiempo promedio de demora de los clientes:', simulacion.getAverageCustomerDelay())    


def runSimulations(count):
    i=0
    while i < count:
        simulacion = Sim(i,SERVER_STATUS.DISPONIBLE.value,EVENT_TYPE.UNKNOWN.value,0.0,0.0,0.0,0.0,0.0,0.0,0,0,99999999,7.0,9.0)
        main(simulacion)
        simulaciones.append(simulacion)
        i+=1
    for sim in simulaciones:
        print(pprint(vars(sim)))
        print('Cantidad promedio de clientes en cola:', sim.getMeanOfClientsInQueue())
        print('Promedio de utilizacion del servidor:', sim.getMeanOfServerUtilization())        
        print('Tiempo promedio de demora de los clientes:', sim.getAverageCustomerDelay())


runSimulations(1)