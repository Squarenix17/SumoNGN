from email.policy import default
import os
import string
import sys
import optparse
import datetime
from numpy import double

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

        vehicle = traci.vehicle.getIDList()
        for i in vehicle:
            bus = i.split('_')
            line = bus[0]
            depTime = bus[1]
            route = bus[2]
            
            
            print("BUS - LINE: " + str(line[1:]) + " DEPART: " + str(depTime[1:]) + " POSITION: " + str(traci.vehicle.getPosition(i)))

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
