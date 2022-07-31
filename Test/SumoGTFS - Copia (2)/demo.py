from email.policy import default
import os
import string
import sys
import optparse
import datetime
import test
from numpy import double, equal

from pandas import options

if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                        default=False, help="run the commandLine version of sumo")
    options, args = opt_parser.parse_args()
    return options

def run():
    step = 0
     
    
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        print(str(datetime.timedelta(seconds = double(traci.simulation.getTime())))+"   N bus: ", end="")
        print(traci.vehicle.getIDCount())

        allBus = []

        vehicle = traci.vehicle.getIDList()
        for x in vehicle:
                buss = x.split('_')
                linee = buss[0]
                depTimee = buss[1]
                routee = buss[2]
                currentBus = [str(linee[1:]), str(depTimee[1:])]
                allBus.append(currentBus)
                #print("BUS - LINE: " + str(linee[1:]) + " DEPART: " + str(depTimee[1:]) + " POSITION: " + str(traci.vehicle.getPosition(x)))

        for k in allBus:
            print(allBus)

        for i in vehicle:
            bus = i.split('_')
            line = bus[0]
            depTime = bus[1]
            route = bus[2]
            #print("BUS - LINE: " + str(line[1:]) + " DEPART: " + str(depTime[1:]) + " POSITION: " + str(traci.vehicle.getPosition(i)))
            
            isNear = True
            for j in vehicle:
                distance = test.getDistance(traci.vehicle.getPosition(i), traci.vehicle.getPosition(j))
                if i == j:
                    continue
                if distance <= 20:
                    if isNear:
                        print("The nearest buses to: Line" + str(line[1:]) + " dTime " + str(depTime[1:]))
                        isNear = False
                    otherBus = j.split('_')
                    lineOB = otherBus[0]
                    depTimeOB = otherBus[1]
                    print("LINE: " + str(lineOB[1:]) + " DEPART: " + str(depTimeOB[1:]) + "is " + str(distance) + "[m] distant")
        #print(traci.vehicle.getIDList())
        
        #print(step)
        step+=1

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
