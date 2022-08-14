import os
import sys
import optparse
import datetime
import support
import traci
import gSheetsManager

from numpy import double, equal
from pandas import options
from email.policy import default
from sumolib import checkBinary

if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                        default=False, help="run the commandLine version of sumo")
    options, args = opt_parser.parse_args()
    return options

def run():

    step = 0
    connectedBus = []
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        #Print number of buses and simulation's current time
        
        print(str(datetime.timedelta(seconds = double(traci.simulation.getTime())))+"   N bus: ", end="")
        print(traci.vehicle.getIDCount(), end="")
        print(" e sono connessi: " + str(connectedBusNow) + " bus")
        connectedBusNow = 0

        #get the list of all vehicle in the simulation
        vehicle = traci.vehicle.getIDList()

        
        for i in vehicle:
            bus = i.split('_')
            line = bus[0]
            depTime = bus[1]

            for j in vehicle:
                distance = support.getDistance(traci.vehicle.getPosition(i), traci.vehicle.getPosition(j))

                if i == j:
                    continue

                if distance <= 20:
                    otherBus = j.split('_')
                    lineOB = otherBus[0]
                    depTimeOB = otherBus[1]    
                    connectedBusNow = connectedBusNow + 1
                    

                    #if the list with the main bus doesn't exist, it's created 
                    if support.inList(str(line) + "_" +str(depTime), connectedBus) == None:
                        #print("LISTA ASSENTE, LA CREO")
                        addBus = [str(line) + "_" +str(depTime), 
                                    {str(lineOB) + "_" +str(depTimeOB):[1, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]}]
                        connectedBus.append(addBus)
                    
                    #if the list exist, but the connected bus isn't in the dictionary, the dictionary is created  
                    elif support.inDictionary(str(lineOB) + "_" +str(depTimeOB), connectedBus[support.inList(str(line) + "_" +str(depTime), connectedBus)]) == False:
                        #print("DIZIONARIO ASSENTE, LO CREO")
                        addDictionary = {str(lineOB) + "_" +str(depTimeOB):[1, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]}
                        connectedBus[support.inList(str(line) + "_" +str(depTime), connectedBus)][1].update(addDictionary)

                    #if the list and the dictionary exist, the conncetion time is increased 
                    elif support.inDictionary(str(lineOB) + "_" +str(depTimeOB), connectedBus[support.inList(str(line) + "_" +str(depTime), connectedBus)]):
                        #print("STESSO DIZIONARIO, AGGIORNO IL TEMPO")
                        time = connectedBus[support.inList(str(line) + "_" +str(depTime), connectedBus)][1].get(str(lineOB) + "_" +str(depTimeOB))[0]+1
                        meatingTime = connectedBus[support.inList(str(line) + "_" +str(depTime), connectedBus)][1].get(str(lineOB) + "_" +str(depTimeOB))[1]
                        
                        addDictionary = {str(lineOB) + "_" +str(depTimeOB):[time, meatingTime]}
                        connectedBus[support.inList(str(line) + "_" +str(depTime), connectedBus)][1].update(addDictionary)
                    #print(connectedBus)
        
        if connectedBus != [] and step >= 3600:
            gSheetsManager.updateSheet(connectedBus)
            step = 1         
        elif step >= 3600:
            step = 1
        else:
            step +=1

        
        
             

    traci.close()
    sys.stdout.flush()


if __name__ == "__main__":
    options = get_options()
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else: 
        sumoBinary = checkBinary('sumo-gui')
    
    traci.start([sumoBinary, "-c", "osm.sumocfg"])
    
    run()

