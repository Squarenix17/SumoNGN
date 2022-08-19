# Tutorial Progetto SUMO - Come Ricreare la Simulazione

## Indice
- [Introduzione](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#introduzione)
- [OSM Web Wizard](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#osm-web-wizard)
  - [Requisiti](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#requisiti)
- [Generazione ed esecuzione dello scenario](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#generazione-ed-esecuzione-dello-scenario)
- [GTFS](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#gtfs)
  - [Calcolo percorso più breve](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#calcolo-percorso-pi%C3%B9-breve)
  - [Percorso da OSM](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#percorso-da-osm)
- [Traci](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#traci)
  - [Utilizzo di TraCI](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#utilizzo-di-traci)
  - [TraCI Protocol](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#traci-protocol)
  - [TraCI - Messaggio TCP](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#traci---messaggio-tcp)
  - [Interfacciare TraCI con Python](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#interfacciare-traci-con-python)
- [Google Sheet](https://github.com/Squarenix17/SumoNGN/tree/main/tutorial#google-sheet)

## Introduzione

La creazione della simulazione PT consiste in tre fasi:
- Requisiti di rete iniziali (OSM)
- Trovare un'origine dati per GTFS
- Mappatura dei dati GTFS sulla rete

## OSM Web Wizard


<p align="justify"><a href="https://sumo.dlr.de/docs/Tutorials/OSMWebWizard.html" title="Console"> OSM Web Wizard</a> offre una delle soluzioni più semplici per lavorare con SUMO. Sulla base di una selezione di un estratto della mappa da openstreetmap, è possibile configurare una domanda di traffico randomizzata ed eseguire e visualizzare lo scenario nel sumo-gui. Questo tutorial ti guiderà passo dopo passo dalla selezione dell'estratto della mappa alla definizione della domanda di traffico attraverso l'esecuzione e la visualizzazione dello scenario in sumo-gui.
 

### Requisiti

- Installazione di SUMO 
- Installazione di Python con versione >= 2.7

<p align="justify">OSM Web Wizard è essenzialmente una raccolta di script python che si trovano nella directory degli strumenti nella radice di installazione di sumo. 
Per avviare OSM Web wizard è sufficiente invocare il seguente comando:

```python osmWebWizard.py```


<p align="justify">Per gli utenti Windows è possibile avviarlo facendo clic su Tutti i programmi -> SUMO -> OSM Web Wizard. Una volta eseguito lo script, dovrebbe aprirsi una pagina web che mostra un estratto della mappa del centro di Berlino.

<img src="/image/screen22.png">

<p align="justify">Ora è possibile selezionare l'area effettiva per la quale si desidera generare lo scenario di simulazione. La selezione dell'area viene attivata facendo clic sulla casella di controllo Select Area nel pannello blu sul lato destro della mappa.

Questa l’area della città di Trento selezionata:

<img src="/image/screen23.png">

<p align="justify">Attenzione: se l'estratto della mappa copre un'area molto ampia, la simulazione potrebbe diventare lenta o addirittura non rispondere.
S<p align="justify">UMO supporta diversi mezzi di trasporto. Nel pannello di generazione della domanda è possibile attivare/disattivare le singole modalità di trasporto facendo clic sulle caselle di controllo corrispondenti.
<p align="justify">Nel nostro progetto abbiamo incluso esclusivamente Bus come mezzi di trasporto

## Generazione ed esecuzione dello scenario
<p align="justify">Lo scenario completo verrà generato automaticamente dopo aver fatto clic su Generate scenario nel pannello di controllo. Una volta terminato il processo di generazione dello scenario, si avvia sumo-gui ed è possibile avviare la simulazione premendo il pulsante Play.

<img src="/image/scree24.png" width=500>

## [GTFS](https://sumo.dlr.de/docs/Tutorials/GTFS.html)

<p align="justify">Questa sezione mostra come perfezionare lo scenario di simulazione del Trasporto Pubblico (PT) esistente con i dati nel formato <a href="https://developers.google.com/transit/gtfs"> GTFS</a> (General Transit Specification Format), disponibile per molte regioni.

Per questo tutorial è stato scelto il giorno 15/07/2022 e di importare solamente bus.


I file GTFS devono essere in formato zip e contenere almeno 
- route.txt
- stop.txt
- stop_times.txt
- trips.txt
- calendar.txt
- calendar_dates.txt 

Per il nostro progetto abbiamo reperito i file GTFS da Trentino Trasporti:
https://www.trentinotrasporti.it/open-data

Per comodità rinominiamo il file zip da google_transit_urbano_tte.zip a TT-GTFS.zip

A seconda dei file di input disponibili, puoi scegliere tra due diversi modi per generare i percorsi.
- Calcolo del percorso più breve
- Percorso da OSM
### Calcolo percorso più breve
In questo caso, il percorso per i bus sarà definito trovando il percorso più veloce tra le fermate.

```python gtfs2pt.py -n osm.net.xml --gtfs TT-GTFS.zip --date 20220715 --modes bus --vtype-output pt_vtypes.xml```

Consigliamo di copiare i tre file: gtfs2fcd.py, gtfs2osm.py e gtfs2pt.py presenti nella repositoriy ed inserirli nella cartella del proprio progetto dove sono presenti i file ottenuti tramite il tool [osmWebWizard](https://sumo.dlr.de/docs/Tools/Import/GTFS.html)

Lo script viene eseguito per circa cinque minuti e genera diverse sottodirectory ma alla fine fornisce tre file di output:

- pt_vtypes.xml
- gtfs_publictransport.add.xml (definizione dei percorsi statici e delle fermate)
- gtfs_publictransport.rou.xml (definizione dei singoli mezzi di trasporto pubblico)

L'output di vtypes genera definizioni molto semplici del tipo di veicolo per le diverse modalità di trasporto pubblico in uso. 

```sumo-gui -n osm.net.xml --additional pt_vtypes.xml,gtfs_publictransport.add.xml,gtfs_publictransport.rou.xml```

### Percorso da OSM
<p align="justify">In questo caso, il percorso per ogni veicolo è preso da OSM. Quando abbiamo importato la rete con lo strumento osmWebWizard, abilitiamo l'opzione di "import public transport", che genera automaticamente il file "osm_ptlines.xml" con le linee di trasporto pubblico.

La chiamata è:

```python tools/import/gtfs/gtfs2pt.py -n osm.net.xml --gtfs TT-GTFS.zip --date 20220715 --osm-routes osm_ptlines.xml --repair --modes bus```


Lo script genera quattro file di output:

- gtfs_publictransport.add.xml (definizione delle fermate)
- gtfs_publictransport.rou.xml (definizione dei singoli mezzi di trasporto pubblico)
- gtfs_missing.xml contiene gli elementi (stop e ptLines) dei dati GTFS che non possono essere importati
- invalid_osm_routes.txt contiene gli avvisi e gli errori dalla riparazione delle ptLines

Per eseguire la chiamata della simulazione:

```sumo-gui -n osm.net.xml --additional gtfs_publictransport.add.xml --routes gtfs_publictransport.rou.xml```

## [Traci](https://sumo.dlr.de/docs/TraCI.html)
https://sumo.dlr.de/pydoc/sumolib.html
https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.htm
https://sumo.dlr.de/docs/TraCI.html
https://sumo.dlr.de/docs/TraCI/Protocol.html

<p align="justify">TraCI è l'abbreviazione di "Traffic Control Interface". Dando accesso ad una simulazione del traffico stradale in corso, permette di recuperare i valori degli oggetti simulati e di manipolarne il comportamento "on-line".

### Utilizzo di TraCI
<p align="justify">TraCI utilizza un'architettura client/server basata su TCP per fornire l'accesso a sumo. In tal modo, sumo funge da server che viene avviato con opzioni aggiuntive della riga di comando: --remote-port <INT> dove <INT> è la porta su cui sumo ascolterà le connessioni in entrata.
<p align="justify">Quando TraCI viene avviato utilizzando remote-port, sumo prepara la simulazione ed attende che tutte le applicazioni esterne si colleghino. L’esecuzione di sumo prosegue fino a che il client non richiede la fine della simulazione.

### [TraCI Protocol](https://sumo.dlr.de/docs/TraCI/Protocol.html)
Dopo aver avviato sumo i client si connettono a instaurando una connessione TCP alla porta designata.

<img src="/image/screen25.png" width=500>

<p align="justify">Una volta avviata la simulazione il client invia dei comandi a sumo per controllare lo stato della simulazione, questi comandi possono influenzare il comportamento dei veicoli o possono richiedere dei dettagli sulla simulazione. Sumo risponde singolarmente a ciascun comando. 
<p align="justify">La simulazione procederà solamente una volta che tutti i comandi del client avranno ricevuto risposta. Il client può anche mettere fine alla simulazione utilizzando l’apposito <a href="https://sumo.dlr.de/docs/TraCI/Control-related_commands.html#command_0x7f_close"> comando di chiusura</a>
. La simulazione terminerà alla chiusura del client. 

<img src="/image/screen26.png" width=500>

### TraCI - Messaggio TCP
<p align="justify">Il messaggio TCP è un raccoglitore di comandi o risultati, ogni messaggio pertanto è costituito da un’intestazione che fornisce la sua dimensione complessiva e un insieme di comandi inseriti dietro ad esso. La lunghezza e l'identificatore di ciascun comando sono posto davanti al comando. Esempio:</p>

<img src="/image/screen27.png" width=500>


<p align="justify">In alcuni casi la lunghezza di un singolo comando potrebbe non essere sufficiente, visto che la lunghezza massima del comando è limitata a 255 bit, in questi casi è possibile impostare il campo della lunghezza in ubyte su zero e aggiungendo la lunghezza di un intero.

<p align="justify">Sumo per semplificare l’utilizzo di TraCI fornisce una classe per gestire la connessione con la porta e una per comporre il messaggio. I linguaggi compatibili sono C++, Python e Java.

<p align="justify">Sumo mette a disposizione un package presente nella sezione tools/traci, il quale consente di interagire con la simulazione utilizzando python.

### Interfacciare TraCI con Python
Le funzioni spiegate in modo dettagliato si possono osservare nella [documentazione ufficiale](https://sumo.dlr.de/pydoc/traci.html)

Al fine di comprendere meglio come interfacciare TraCI con Python rimandiamo alla [documentazione ufficiale](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html)
Per utilizzare traci in python, una volta settate correttamente le variabili d’ambiente, è sufficiente utilizzare il comando import traci
## Google Sheet
Per connettere lo script a un file su Google Sheet bisogna andare sulla <a href="https://console.developers.google.com/" title="Console">
console per sviluppatori di google</a> e creare un nuovo progetto, cliccando nel menù a tendina a destra della scritta Google Cloud

<img src="/image/screen1.png" width=500>

<img src="/image/screen2.png" width=500>

Creare un progetto:

<img src="/image/screen3.png" width=500>

Una volta nella dashboard del  progetto, cercare nella barra di ricerca: Google Sheets API

<img src="/image/screen4.png" width=500>

<img src="/image/screen5.png" width=500>

Ed abilitare le API, fare la stessa cosa per le API di Google Drive

<img src="/image/screen6.png" width=500>

Recandosi nella dashboard selezionare Service Accounts

<img src="/image/screen7.png" width=500>

E creare un nuovo service account

<img src="/image/screen8.png" width=500>

<img src="/image/screen9.png" width=500>

premere create and continue e selezionare il ruolo Editor:

<img src="/image/screen10.png" width=500>

Una volta creato cliccare l’email del Service Account

<img src="/image/screen11.png" width=500>

Recandosi in Keys

<img src="/image/screen12.png" width=500>

è necessario creare una nuova chiave privata in json:

<img src="/image/screen13.png" width=500>

Questo file andrà rinominato in token.json ed inserito nella cartella del programma.

<img src="/image/screen14.png" width=500>


<p align="justify">Ora sarà necessario creare il foglio di calcolo su Google docs, il quale è importante che venga rinominato Sumo Data (Con nomi differenti la simulazione non funzionerà), noi consigliamo semplicemente di creare una copia del file da noi creato: <a href="https://docs.google.com/spreadsheets/d/1YQGfxctZY_-qP6vxARLi4rUKwdY9jNnQ538quYU-xm4/edit#gid=477510729/"> Sumo Data</a>

<p align="justify">Nella copia del file Sumo Data è importante condividere l’accesso con la mail del Service Account creato in precedenza: 

<img src="/image/screen15.png" width=500>


<p align="justify">Se sono stati eseguiti tutti i passaggi correttamente è ora possibile lanciare la simulazione utilizzando il file runner.py 

<img src="/image/screen16.png" width=500>

Si aprirà in automatico il file Google Sheet Sumo Data

<img src="/image/screen17.png" width=500>

e per far partire la simulazione sarà necessario premere sulla freccia verde Run

<img src="/image/screen18.png" width=500>

<p align="justify">per velocizzare la simulazione suggeriamo di ridurre il Delay a 0 e impostare la visualizzazione della mappa in faster standard</p>

<img src="/image/screen19.png" width=500>

si apre anche la finestra dello script python che contiene:
- Orario
- Numero bus presenti sulla mappa
- Numero di bus connessi tra loro

<img src="/image/screen20.png" width=500>

e man mano che il programma rileva le connessioni tra i bus le trascriverà sul file Google Sheet indicando 
- Nome del bus principale
- Nome del bus che viene incontrato
- Tempo per il quale rimangono connessi
- Orario in cui avviene l’incrocio

<img src="/image/screen21.png" width=500>
  
<p align="justify">L’aggiornamento sul foglio di calcolo avviene ogni 1800 secondi (30 minuti) trascorsi all’interno della simulazione.</p>