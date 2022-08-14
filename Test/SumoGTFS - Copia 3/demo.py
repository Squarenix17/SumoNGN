from email.policy import default
import os
import string
import sys
import optparse
import datetime
import gspread
from tokenize import cookie_re
import test
from numpy import double, equal
from pandas import options

import pandas as pd

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
     
    connectedBus = []
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        print("   [ Orario: ",end="")
        print(str(datetime.timedelta(seconds = double(traci.simulation.getTime())))+" ]     [ N bus in circolazione: ", end="")
        print(traci.vehicle.getIDCount(), end="")
        print(" ] ")
        allBus = []

        vehicle = traci.vehicle.getIDList()
        for x in vehicle:
                buss = x.split('_')
                linee = buss[0]
                depTimee = buss[1]
                routee = buss[2]
                currentBus = [str(linee) + "_" +str(depTimee)]
                allBus.append(currentBus)
                #print("BUS - LINE: " + str(linee[1:]) + " DEPART: " + str(depTimee[1:]) + " POSITION: " + str(traci.vehicle.getPosition(x)))

        
        

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
                    otherBus = j.split('_')
                    lineOB = otherBus[0]
                    depTimeOB = otherBus[1]
                    
                    #print(test.inList(str(line) + "_" +str(depTime), connectedBus))
                    if test.inList(str(line) + "_" +str(depTime), connectedBus) == None:
                        createDictionary = {str(lineOB) + "_" +str(depTimeOB):1}
                        #addBus = [str(line) + "_" +str(depTime), [{str(lineOB) + "_" +str(depTimeOB):[1, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]}]]
                        print("LISTA ASSENTE, LA CREO")
                        addBus = [str(line) + "_" +str(depTime), {str(lineOB) + "_" +str(depTimeOB):[1, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]}]
                        connectedBus.append(addBus)
                    elif test.inDictionary2(str(lineOB) + "_" +str(depTimeOB), connectedBus[test.inList(str(line) + "_" +str(depTime), connectedBus)]) == False:
                        print("DIZIONARIO ASSENTE, LO CREO")
                        #connectedBus[test.inList(str(line) + "_" +str(depTime), connectedBus)].append({str(lineOB) + "_" +str(depTimeOB):[1, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]})

                        #print("STESSO BUS")
                        #print(str(line) + " " + str(depTime) + "    " + str(lineOB) + str(depTimeOB))
                        #print("Poszione Da aggingere: " + str(test.inList(str(line) + "_" +str(depTime), connectedBus)))
                        dictionary = {str(lineOB) + "_" +str(depTimeOB):[1, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]}
                        connectedBus[test.inList(str(line) + "_" +str(depTime), connectedBus)][1].update(dictionary)
                        #print(dictionary)
                        
                    elif test.inDictionary2(str(lineOB) + "_" +str(depTimeOB), connectedBus[test.inList(str(line) + "_" +str(depTime), connectedBus)]):
                        print("STESSO DIZIONARIO, AGGIORNO IL TEMPO")
                        #print(str(line) + " " + str(depTime) + "    " + str(lineOB) + str(depTimeOB))
                        #print("Posizione del Dizionario: " + str(test.dictionaryPos(str(lineOB) + "_" +str(depTimeOB), connectedBus[test.inList(str(line) + "_" +str(depTime), connectedBus)])))
                        
                        time = connectedBus[test.inList(str(line) + "_" +str(depTime), connectedBus)][1].get(str(lineOB) + "_" +str(depTimeOB))[0]+1
                        dictionary = {str(lineOB) + "_" +str(depTimeOB):[time, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]}
                        connectedBus[test.inList(str(line) + "_" +str(depTime), connectedBus)][1].update(dictionary)
                        
                    print(connectedBus)   
                    
                    # Esportazione Excel

                    #data = {'Bus 1':[connectedBus[0][0]],
                    #        'Bus 2':[dictionary],
                    #        'Orario Inc':[depTimeOB],
                    #        'Tempo conn':[depTime]
                    #       }
                    #df = pd.DataFrame(connectedBus)
                    #dfexcel = pd.ExcelWriter('DatabaseBus.xlsx',engine='xlsxwriter')
                    #df.to_excel(dfexcel,sheet_name='rilevazione1')
                    #dfexcel.save()
                    #print(' ')
                    #print('INCROCIO BUS SALVATO SU EXCEL')


                    # Esportazione Fogli

                    #sa = gspread.service_account()
                    #sh = sa.open("Test SUMO")
                    #wks = sh.worksheet("Foglio1")
                    #print(wks.acell('A2').value)
                    #wks.update('A3', "Qua vanno fatti entrare i file")



                    # if isNear:
                    #     print("The nearest buses to: Line" + str(line[1:]) + " dTime " + str(depTime[1:]))
                    #     isNear = False
                    
                    # print("LINE: " + str(lineOB[1:]) + " DEPART: " + str(depTimeOB[1:]) + "is " + str(distance) + "[m] distant")
        #print(traci.vehicle.getIDList())
        #print(connectedBus)
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