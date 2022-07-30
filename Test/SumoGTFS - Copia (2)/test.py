import math
from turtle import distance

from numpy import mat


def getDistance(mainBusPos, otherBusPos):
    
    Xcoord = mainBusPos[0] - otherBusPos[0]
    Ycoord = mainBusPos[1] - otherBusPos[1]


    distance = round(math.sqrt(math.pow(Xcoord,2)+math.pow(Ycoord, 2)),2)

    return distance


coord1 = (3.50, 8.75)
coord2 = (7.69, 7.853)

print(getDistance(coord1, coord2))