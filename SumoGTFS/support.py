import math
from operator import index
from turtle import distance
from itertools import chain
from numpy import mat

def getDistance(mainBusPos, otherBusPos):
    Xcoord = mainBusPos[0] - otherBusPos[0]
    Ycoord = mainBusPos[1] - otherBusPos[1]
    distance = round(math.sqrt(math.pow(Xcoord,2)+math.pow(Ycoord, 2)),2)
    return distance

def inList(bus, connectedBusList):
    pos = next(((i, l.index(bus)) for i, l in enumerate(connectedBusList) if bus in l), None)
    if pos == None:
        return None
    return pos[0]

def inDictionary(otherBus, connectedBusList):
    if otherBus in connectedBusList[1]:
        return True
    return False