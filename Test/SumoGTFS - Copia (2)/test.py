import math
from turtle import distance

from numpy import mat


def getDistance(mainBusPos, otherBusPos):
    
    Xcoord = mainBusPos[0] - otherBusPos[0]
    Ycoord = mainBusPos[1] - otherBusPos[1]


    distance = round(math.sqrt(math.pow(Xcoord,2)+math.pow(Ycoord, 2)),2)

    return distance

def inList(bus, connectedBusList):
    for i, sublist in enumerate(connectedBusList):
        if bus in sublist:
            return i
        return -1


coord1 = (3.50, 8.75)
coord2 = (7.69, 7.853)

print(getDistance(coord1, coord2))


listaA = ["a", "b", "c"]
listaB = ["d", "e"]

lista = [listaA, listaB]

lista2 = ["Linea+dep", [{"lconn":[1,"8:05"]}]]



if any(d.get("lconn") for d in lista2[1]):
    print("si")


