# **Progetto SUMO**
## Next Generation Networks 

Docente del corso:

Fabrizio Granelli 


**Yousef Soliman Mekheimar - Gabriele Ughetto**

# Indice
- [Introduzione](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#introduzione)
- [Tutorial Progetto SUMO - Come Avviare la Simulazione](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#tutorial-progetto-sumo---come-avviare-la-simulazione)
  - [Introduzione](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#introduzione-1)
  - [Requisiti](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#requisiti)
  - [Procedura](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#procedura)
  - [Google Sheet](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#google-sheet)
- [Tutorial Progetto SUMO - Come Ricreare la Simulazione](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#tutorial-progetto-sumo---come-ricreare-la-simulazione)
- [Descrizione Codice](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#descrizione-codice)
  - [Introduzione](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#introduzione-2)
  - [File runner.py](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#file-runnerpy)
  - [File support.py](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#file-supportpy)
  - [File gSeetsManager.py](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#file-gseetsmanagerpy)
  - [File osm.sumocfg](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#file--osmsumocfg)
- [Problematiche](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#problematiche)
  - [Mappa con connessioni imprecise o interrotte](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#mappa-con-connessioni-imprecise-o-interrotte)
  - [Simulazione pesante](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#simulazione-pesante)
  - [Modifica del file *gtfs_publictransport.rou.xml*](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#modifica-del-file-gtfs_publictransportrouxml)
  - [Aggiornamento API](https://github.com/Squarenix17/SumoNGN/blob/main/README.md#aggiornamento-api)



# Introduzione

<img src="image/app.png">

<p align="justify">Il progetto realizzato permette di ottenere un riscontro sulle interconnessioni degli autobus della città di Trento, fornisce il numero di incroci, l’orario di incrocio e il tempo di connessione tra due bus che si incrociano in un area di diametro 20 metri.</p>

<img src="image/bus1.png" width=500>

La struttura del progetto si può suddividere in quattro fasi:
- Setting e requisiti di Network iniziali 
- Ricerca e mappatura dati GTFS sul Network
- Elaborazione dei dati con Python e TraCI
- Esportazione dei risultati su Google Sheet

<img src="image/struct.png" width=500>


# Tutorial Progetto SUMO - Come Avviare la Simulazione
## Introduzione:
<p align="justify">Una volta clonata la repository nel proprio computer è possibile lanciare la simulazione presente nel progetto, realizzata in python, avviando il file runner.py presente nella cartella, una volta che sono soddisfatti i requisiti necessari.</p>

## Requisiti:

Per avviare la simulazione sopracitata è necessario rispettare i seguenti requisiti:
- [Sumo](https://sumo.dlr.de/docs/Installing/index.html)
- [Python 3.X](https://www.python.org/downloads/)
- Tool di python necessari: Pandas, gspread 
- Account [Developer su Google](https://developers.google.com/)

## Procedura:

<p align="justify">Installare SUMO seguendo dettagliatamente la documentazione, facendo attenzione ad impostare correttamente i path nelle variabili di sistema.</p>

<p align="justify">Su Windows sconsigliamo di installare SUMO nelle Cartelle Program Files o Program Files(x86) poiché possono esserci dei conflitti se vengono avviate simulazioni senza permessi di amministratore. Installando SUMO ad esempio nella cartella utente non si presentano queste problematiche.
IMPORTANTE alle variabili di sistema è necessario aggiungere "/your/path/to/sumo/tools"      PYTHONPATH
Installare Python ed i moduli utilizzando PIP, il package installer di Python per la versione che si intende utilizzare per lanciare la simulazione.</p>

## Google Sheet:

<p align="justify">Dalla <a href="https://console.developers.google.com/" title="Console"> console per sviluppatori di google</a> è necessario creare un nuovo progetto, cliccando nel menù a tendina a destra della scritta Google Cloud </p>


<img src="image/screen1.png" width=500>

<img src="image/screen2.png" width=500>

Creare un progetto:

<img src="image/screen3.png" width=500>

Una volta nella dashboard del  progetto, cercare nella barra di ricerca: Google Sheets API

<img src="image/screen4.png" width=500>

<img src="image/screen5.png" width=500>

Ed abilitare le API, fare la stessa cosa per le API di Google Drive

<img src="image/screen6.png" width=500>

Recandosi nella dashboard selezionare Service Accounts

<img src="image/screen7.png" width=500>

E creare un nuovo service account

<img src="image/screen8.png" width=500>

<img src="image/screen9.png" width=500>

premere create and continue e selezionare il ruolo Editor:

<img src="image/screen10.png" width=500>

Una volta creato cliccare l’email del Service Account

<img src="image/screen11.png" width=500>

Recandosi in Keys

<img src="image/screen12.png" width=500>

è necessario creare una nuova chiave privata in json:

<img src="image/screen13.png" width=500>

Questo file andrà rinominato in token.json ed inserito nella cartella del programma.

<img src="image/screen14.png" width=500>


<p align="justify">Ora sarà necessario creare il foglio di calcolo su Google docs, il quale è importante che venga rinominato Sumo Data (Con nomi differenti la simulazione non funzionerà), noi consigliamo semplicemente di creare una copia del file da noi creato: <a href="https://docs.google.com/spreadsheets/d/1YQGfxctZY_-qP6vxARLi4rUKwdY9jNnQ538quYU-xm4/edit#gid=477510729/"> Sumo Data</a>

<p align="justify">Nella copia del file Sumo Data è importante condividere l’accesso con la mail del Service Account creato in precedenza:</p> 

<img src="image/screen15.png" width=500>


<p align="justify">Se sono stati eseguiti tutti i passaggi correttamente è ora possibile lanciare la simulazione utilizzando il file runner.py 

<img src="image/screen16.png" width=500>

Si aprirà in automatico il file Google Sheet Sumo Data

<img src="image/screen17.png" width=500>

e per far partire la simulazione sarà necessario premere sulla freccia verde Run

<img src="image/screen18.png" width=500>

<p align="justify">per velocizzare la simulazione suggeriamo di ridurre il Delay a 0 e impostare la visualizzazione della mappa in faster standard</p>

<img src="image/screen19.png" width=500>

si apre anche la finestra dello script python che contiene:
- Orario
- Numero bus presenti sulla mappa
- Numero di bus connessi tra loro

<img src="image/screen20.png" width=500>

e man mano che il programma rileva le connessioni tra i bus le trascriverà sul file Google Sheet indicando 
- Nome del bus principale
- Nome del bus che viene incontrato
- Tempo per il quale rimangono connessi
- Orario in cui avviene l’incrocio

<img src="image/screen21.png" width=500>

<p align="justify">L’aggiornamento sul foglio di calcolo avviene ogni 1800 secondi (30 minuti) trascorsi all’interno della simulazione.</p>


# [Tutorial Progetto SUMO - Come Ricreare la Simulazione](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#tutorial-progetto-sumo---come-ricreare-la-simulazione)
 
# Descrizione Codice
## Introduzione
Il codice descritto in questa sezione funziona esclusivamente per il file *gtfs_publictransport.rou.xml* presente in questa simulazione, l’id dei veicoli è stato infatti modificato come in sequente esempio: `vehicle id="lNumeroLinea_dOrarioPartenza_rNumeroRoute”` 
Il file di partenza ottenuto dai file GTFS l’id del veicolo era esclusivamente *NumeroRoute*

## File runner.py
Il fine *runner.py* è il file che permette di lanciare la simulazione e consente la comunicazione attraverso TraCI, lo script è composto nel seguente modo:
Inizialmente vengono importati i seguenti moduli
```python
import os
import sys
import optparse
import datetime
import support
import traci
import gSheetsManager
 
from numpy import double
from pandas import options
 
from sumolib import checkBinary
```

In accordo con la [documentazione ufficiale](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html), è consigliato introdurre una struttura condizionale che restituisce un errore qualora non fosse impostata correttamente la variabile d’ambiente *SUMO_HOME*.
```python
if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")
```

La funzione *get_options()* ritorna l’opzione che permette di lanciare la simulazione con o senza *gui*.
```python
def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                        default=False, help="run the commandLine version of sumo")
    options, args = opt_parser.parse_args()
    return options
```
La funzione *run()* è responsabile della comunicazione tra lo script e SUMO, per fare ciò viene utilizzato TraCI.
```python
def run():
    connectedBusNow = 0
    step = 0
    connectedBus = []
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
```
Il while proseguirà fino a che [*getMinExpectedNumber()*](https://sumo.dlr.de/pydoc/traci._simulation.html#SimulationDomain-getMinExpectedNumber) ritornerà 0, ciò significherà che tutti gli elementi della simulazione sono stati analizzati e non sarà più necessario proseguire. Ogni ciclo while corrisponde ad 1 secondo all’interno della simulazione.
Mentre attraverso la funzione *simulationStep()* traci acquisirà tutti gli elementi del ciclo corrente, come veicoli e tempo. La presenza della funzione permette allo script di acquisire le informazioni della simulazione.

```python
        print(str(datetime.timedelta(seconds = double(traci.simulation.getTime())))+"   N bus: ", end="")
        print(traci.vehicle.getIDCount(), end="")
        print(" e sono connessi: " + str(connectedBusNow) + " bus")
        connectedBusNow = 0
 
        vehicle = traci.vehicle.getIDList()
```
Nella console dello script per ogni ciclo verranno stampati: l’orario, il numero di bus presenti nella simulazione ed il numero di bus connessi nel ciclo corrente. Inoltre in una lista vengono salvati tutti i nomi dei veicoli presenti nel ciclo corrente.

```python
        for i in vehicle:
            bus = i.split('_')
            line = bus[0]
            depTime = bus[1]
            currentBus = str(line) + "_" +str(depTime)
```
Il primo *for* scorre la lista dei veicoli e divide l’id, utilizzando come divisore l’underscore, in una lista *bus*. 

```python
            for j in vehicle:
                distance = support.getDistance(traci.vehicle.getPosition(i), traci.vehicle.getPosition(j))
                    if i == j:
                        continue
```
Successivamente è presente un altro for nidificato al primo, in questo caso viene nuovamente scorsa la lista dell’*id* dei veicoli, viene salvata la distanza tra il veicolo *i* ed il veicolo *j* in una variabile *distance* utilizzando una funzione del file *support*, la quale riceve in ingresso la posizione dei due veicoli attraverso la funzione [*getPosition()*](https://sumo.dlr.de/pydoc/traci._vehicle.html#VehicleDomain-getPosition). L’*if* presente salterà al ciclo successivo se i due veicoli risultassero uguali.

```python
            if distance <= 20:
                    otherBus = j.split('_')
                    lineOB = otherBus[0]
                    depTimeOB = otherBus[1]    
                    connectedBusNow = connectedBusNow + 1
                    currentConnectedBus = str(lineOB) + "_" +str(depTimeOB)
```
Il secondo *if* presente verificherà che la distanza tra i due veicoli sia minore uguale a 20 metri, se così fosse, viene suddiviso anche il bus presente in *j* con lo stesso criterio del veicolo *i*.

### Struttura della lista connectedBus
Nella lista *connectedBus* verranno salvati tutti i veicoli ed è organizzata nel seguente modo:
```python
   connctedBus=[[BusPrincipale, {BusConnesso:[TempoDiConnessione, OrarioInizioConnessione]}]]
```
è una lista contenente un’altra lista la quale è strutturata come:
- Posizione 0: Bus principale, nel ciclo *for* nidificato corrisponde ad *i*;
- Posizione 1: è un dizionario che contiene i dettagli delle connessioni

Il dizionario è a sua volta organizzato come:
- Chiave: corrisponde al Bus secondario, connesso al primo, corrisponde a *j* nel ciclo *for* nidificato;
- Valore: Il valore della chiave è una lista contente; alla posizione 0 il tempo totale della connessione tra i due autobus, mentre nella posizione 1 è presente l’orario della prima connessione tra i due mezzi.
Al dizionario possono aggiungersi più chiavi nel caso l’autobus principale incontrasse più veicoli durante la sua corsa.

Proseguendo con la descrizione del ciclo *for* nidificato:
```python
                    if support.inList(currentBus, connectedBus) == None:
                          addBus = [currentBus, {currentConnectedBus:[1, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]}]
                          connectedBus.append(addBus)
```
Il primo *if* successivo alla verifica della distanza inferiore a 20[m] verifica se all’interno di *connectedBus*, sia presente una lista con l’autobus principale, utilizzando una funzione del file *support*, nel caso non fosse presente viene creata.

```python
                    elif support.inDictionary(currentConnectedBus, connectedBus[support.inList(currentBus, connectedBus)]) == False:
                         addDictionary = {currentConnectedBus:[1, str(datetime.timedelta(seconds = double(traci.simulation.getTime())))]}
                         connectedBus[support.inList(currentBus, connectedBus)][1].update(addDictionary)
```
La seconda struttura condizionale è un *elif*, per cui se se esiste in *connctedBus* una lista con l’autobus *i*, viene verificata la presenza del dizionario con l’autobus secondario, nel caso mancasse viene creato il dizionario ed il suo valore, con orario corrispondente al ciclo while in cui si trova la simulazione.

```python
                    elif support.inDictionary(currentConnectedBus, connectedBus[support.inList(currentBus, connectedBus)]):
                        time = connectedBus[support.inList(currentBus, connectedBus)][1].get(currentConnectedBus)[0]+1
                        meatingTime = connectedBus[support.inList(currentBus, connectedBus)][1].get(currentConnectedBus)[1]
                        addDictionary = {currentConnectedBus:[time, meatingTime]}
                        connectedBus[support.inList(currentBus, connectedBus)][1].update(addDictionary)
```
La terza ed ultima struttura condizionale conferma la presenza della lista con con l’autobus principale e il dizionario con l’autobus secondario, per cui viene incrementato il tempo di connessione tra i due autobus.

```python
       if connectedBus != [] and step >= 1800:
            gSheetsManager.updateSheet(connectedBus)
            step = 1        
        elif step >= 1800:
            step = 1
        else:
            step +=1             
```
Al di fuori dei due cicli *for* nidificati si trova la struttura condizionale responsabile dell’aggiornamento del foglio di calcolo, che avviene ogni 1800 secondi (cicli while) all’interno della simulazione. L’aggiornamento del foglio di calcolo avviene tramite una funzione dello script *gSheetsManager*.

```python
       traci.close()
       sys.stdout.flush()             
```
Al di fuori del ciclo while si trovano i comandi per terminare la connessione TraCI e la simulazione.

```python
if __name__ == "__main__":
    options = get_options()
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
   
    traci.start([sumoBinary, "-c", "osm.sumocfg"])
   
    run()            
```
Al di fuori della funzione *run()* si trova il main, che avvierà o meno la gui a seconda delle opzioni ed assocerà alla simulazione il file *osm.sumocfg* il quale conterrà i file da importare nella simulazione. Dopo il lancio della simulazione verrà chiamata la funzione *run()*.

## File support.py
```python
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
```
All’interno del file di supporto saranno presenti 3 funzioni:
- *getDistance(mainBusPos, otherBusPos)*: la funzione calcolerà la distanza tra i due autobus usando la formula della distanza tra 2 punti;
- *inList(bus, connectedBusList)*: verifica la presenza o meno dell’autobus principale all’interno di una lista;
- *inDictionary(bus, connectedBusList)*: controlla se nel dizionario è presente l’elemento passato, ovvero l’autobus secondario.   

## File gSeetsManager.py
Il file è responsabile della connessione con le API di google sheet e l’aggiornamento del foglio di calcolo collegato.
```python
import gspread
import webbrowser
 
 
 
def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)
 
def updateSheet(busList):
    lastLine = 1
    for element in busList:
    #print(element[0])
        for key, value in element[1].items():
            lastLine = lastLine + 1
 
    updateRange = "A2:D" + str(lastLine)
    cell_list = wks.range(updateRange)
 
    i = 0
    for element in busList:
        for key, value in element[1].items():
            cell_list[i].value = element[0]
            i = i + 1
            cell_list[i].value = key
            i = i + 1
            cell_list[i].value = value[0]
            i = i + 1
            cell_list[i].value = value[1]
            i = i + 1
            range = "C" + str(2) + ":D" + str(i)
            wks.format(range, {"horizontalAlignment": "CENTER"})  
            wks.update_cells(cell_list)
 
sa = gspread.service_account("token.json")
print("Apertura Foglio di Calcolo in Corso!")
#print(sa)
 
sh = sa.open("Sumo Data")
 
wks = sh.sheet1
webbrowser.open(sh.url)
range =  "A2:D" + str(next_available_row(wks))
wks.batch_clear([range])
```
Lo script inizialmente instaura una connessione con il foglio di calcolo e cancellerà le celle riempite da dati di simulazioni precedenti. 
Nello script sono presenti 2 funzioni:
- *next_aviable_row(worksheet)*: la funzione restituirà un intero con il numero della prima riga vuota;
- *updateSheet(busList*): la funzione raggrupperà il range di valori da aggiornare e con un’unica chiamata alle API aggiornerà il foglio di calcolo nel range di valori corrispondente a *busList*.

### File  osm.sumocfg
Attraverso questo file è possibile configurare la simulazione impostando file addizionali in accordo con la [documentazione](https://sumo.dlr.de/docs/Simulation/Basic_Definition.html#input_files) 
```xml
<input>
        <net-file value="osm.net.xml"/>
        <additional-files value="pt_vtypes.xml,gtfs_publictransport.add.xml,gtfs_publictransport.rou.xml"/>
</input>           
```
I file che abbiamo impiegato in input nella simulazione sono, osm.net.xml che contiene la rete stradale della città di trento. Come file addizionali invece: *pt_vtypes.xml* che contiene la tipologia di veicoli impiegati nella simulazione, *gtfs_publictransport.add.xml* contenente la lista di fermate ed i percorsi che gli autobus effettueranno durante la simulazione ed infine *gtfs_publictransport.rou.xml* il quale è responsabile del percorso che gli autobus devono seguire.

# Problematiche

Durante il progetto abbiamo riscontrato alcune problematiche.

## Mappa con connessioni imprecise o interrotte
Il tool fornito da SUMO osmWebWizard, che consente di selezionare una regione geografica su Open Street Map e convertirla in una rete pronta per essere simulata, presenta delle problematiche per aree molto grandi. Abbiamo tentato gli altri metodi consigliati nella sezione [OSM](https://sumo.dlr.de/docs/Tools/Import/OSM.html) della documentazione, ma la problematica persisteva. La mappa dunque rappresentata non è totalmente fedele a quella della città di Trento e alcuni percorsi degli autobus potrebbero averne risentito con la conseguenza che il percorso simulato non rappresenterà quello reale in alcune zone.

## Simulazione pesante 
La simulazione deve coprire una zona molto vasta con numerose intersezioni, infatti nelle ore in cui sono presenti più autobus, dalle 7:00 alle 16:00 circa, il tempo di computazione che richiede ogni ciclo aumenta in maniera significativa. Al fine di non rendere ulteriormente pensante la simulazione abbiamo deciso di non implementare un traffico generato randomicamente.

## Modifica del file *gtfs_publictransport.rou.xml*
Il file gtfs_publictransport.rou.xml ottenuto dallo script *gtfs2pt.py* utilizzando il GTFS fornito da Trentino Trasporti presentava un id degli autobus poco riconoscibile, pertanto abbiamo modificato manualmente l’id di ogni bus nel seguente modo:
```xml
vehicle id="lNumeroLinea_dOrarioPartenza_rNumeroRoute"
```

## Aggiornamento API
Durante la simulazione l’aggiornamento del foglio di calcolo non avviene ad ogni ciclo, le motivazioni di questa scelta sono due, la prima è il limite di richieste al minuto delle api google, le quali non permettono di stare al passo con l’esecuzione della simulazione. La seconda motivazione riguarda la velocità con cui viene eseguita la richiesta, TraCI infatti prima di proseguire al ciclo successivo attenderà l’avvenuta scrittura nel foglio di calcolo e il tempo di attesa per ogni chiamata è significativo. La chiamata alle API sarà eseguita una sola volta raggruppando tutte le celle da aggiornare.
 
 

