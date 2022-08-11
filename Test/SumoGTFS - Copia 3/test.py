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



def inList4(bus, connectedBusList):
    for i, sublist in enumerate(connectedBusList):
        if bus in sublist:
            return i
        return -1

def inList2(bus, connectedBusList):
    return bus in chain(*connectedBusList)

def inList3(bus, connectedBusList):
    return next(((i, connectedBusList.index(bus))
      for i, bus in enumerate(connectedBusList)
      if c in colour),
     None)


def inDictionary(otherBus, connectedBusList):
    v = next((index for (index, d) in enumerate(connectedBusList[1]) if d.get(otherBus)), None)
    if v == None:
        return False
    return True

def inDictionary2(otherBus, connectedBusList):
    if otherBus in connectedBusList[1]:
        return True
    return False

def dictionaryPos(otherBus, connectedBusList):
    v = next((index for (index, d) in enumerate(connectedBusList[1]) if d.get(otherBus)), None)
    if v == None:
        return None
    return v


coord1 = (3.50, 8.75)
coord2 = (7.69, 7.853)

#print(getDistance(coord1, coord2))


listaA = ["a", "b", "c"]
listaB = ["d", "e"]



lista2 = ["Linea+dep", {"lconn":[1,"8:05"], "aconn":[2,"8:05"], "AAA":[2,"8:05"]}]

lista = [listaA, lista2]

#index = next((index for (index, d) in enumerate(lista2[1]) if d.get("lconn")), None)


lista[1][1].update({"Bus":[3, "5:05"]})

print(lista[1][1].get("AAA")[0]+5)

print(inDictionary2("AAAA", lista[inList("Linea+dep", lista)]))

#print(inDictionary("aconn", lista[inList("Linea+dep", lista)]))
#print(dictionaryPos("Bus", lista[inList("Linea+dep", lista)]))

print(lista2)

# print([(i, l.index("e"))
#  for i, l in enumerate(lista)
#  if "e" in l])

# pos = next(((i, l.index("G"))
#       for i, l in enumerate(lista)
#       if "G" in l),
#      None)

# print(pos)

