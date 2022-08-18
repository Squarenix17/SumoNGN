## Descrizione Codice

### Introduzione
Il codice descritto in questa sezione funziona esclusivamente per il file *gtfs_publictransport.rou.xml* presente in questa simulazione, l’id dei veicoli è stato infatti modificato come in sequente esempio:

vehicle id="lNumeroLinea_dOrarioPartenza_rNumeroRoute”

Il file di partenza ottenuto dai file GTFS l’id del veicolo era esclusivamente *NumeroRoute*

### runner.py
Il fine *runner.py* è il file che permette di lanciare la simulazione e consente la comunicazione attraverso TraCI, lo script è composto nel seguente modo:

Inizialmente vengono importati i seguenti moduli:

CODE

In accordo con la documentazione [ufficiale](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html), è consigliato introdurre una struttura condizionale che restituisce un errore qualora non fosse impostata correttamente la variabile d’ambiente *SUMO_HOME*.

CODE

La funzione *get_options()* ritorna l’opzione che permette di lanciare la simulazione con o senza *gui*.

CODE

La funzione *run()* è responsabile della comunicazione tra lo script e SUMO, per fare ciò viene utilizzato TraCI.

CODE

Il while proseguirà fino a che [*getMinExpectedNumber()*](https://sumo.dlr.de/pydoc/traci._simulation.html#SimulationDomain-getMinExpectedNumber) ritornerà 0, ciò significherà che tutti gli elementi della simulazione sono stati analizzati e non sarà più necessario proseguire. Ogni ciclo while corrisponde ad 1 secondo all’interno della simulazione.
Mentre attraverso la funzione *simulationStep()* traci acquisirà tutti gli elementi del ciclo corrente, come veicoli e tempo. La presenza della funzione permette allo script di acquisire le informazioni della simulazione.

CODE

Nella console dello script per ogni ciclo verranno stampati: l’orario, il numero di bus presenti nella simulazione ed il numero di bus connessi nel ciclo corrente. Inoltre in una lista vengono salvati tutti i nomi dei veicoli presenti nel ciclo corrente.

CODE

Il primo *for* scorre la lista dei veicoli e divide l’id, utilizzando come divisore l’underscore, in una lista *bus*. 

CODE

Successivamente è presente un altro for nidificato al primo, in questo caso viene nuovamente scorsa la lista dell’*id* dei veicoli, viene salvata la distanza tra il veicolo *i* ed il veicolo *j* in una variabile *distance* utilizzando una funzione del file *support*, la quale riceve in ingresso la posizione dei due veicoli attraverso la funzione [*getPosition()*](https://sumo.dlr.de/pydoc/traci._vehicle.html#VehicleDomain-getPosition). L’*if* presente salterà al ciclo successivo se i due veicoli risultassero uguali.

CODE

Il secondo *if* presente verificherà che la distanza tra i due veicoli sia minore uguale a 20 metri, se così fosse, viene suddiviso anche il bus presente in *j* con lo stesso criterio del veicolo *i*. 

### Struttura della lista connectedBus
Nella lista *connectedBus* verranno salvati tutti i veicoli ed è organizzata nel seguente modo:

CODE

è una lista contenente un’altra lista la quale è strutturata come:

- Posizione 0: Bus principale, nel ciclo *for* nidificato corrisponde ad *i*;
- Posizione 1: è un dizionario che contiene i dettagli delle connessioni

Il dizionario è a sua volta organizzato come:
- Chiave: corrisponde al Bus secondario, connesso al primo, corrisponde a *j* nel ciclo *for* nidificato;
- Valore: Il valore della chiave è una lista contente; alla posizione 0 il tempo totale della connessione tra i due autobus, mentre nella posizione 1 è presente l’orario della prima connessione tra i due mezzi.

Al dizionario possono aggiungersi più chiavi nel caso l’autobus principale incontrasse più veicoli durante la sua corsa.

Proseguendo con la descrizione del ciclo *for* nidificato:

CODE

Il primo *if* successivo alla verifica della distanza inferiore a 20[m] verifica se all’interno di *connectedBus*, sia presente una lista con l’autobus principale, utilizzando una funzione del file *support*, nel caso non fosse presente viene creata.

CODE

La seconda struttura condizionale è un *elif*, per cui se se esiste in *connctedBus* una lista con l’autobus *i*, viene verificata la presenza del dizionario con l’autobus secondario, nel caso mancasse viene creato il dizionario ed il suo valore, con orario corrispondente al ciclo while in cui si trova la simulazione.

CODE

La terza ed ultima struttura condizionale conferma la presenza della lista con con l’autobus principale e il dizionario con l’autobus secondario, per cui viene incrementato il tempo di connessione tra i due autobus.

CODE

Al di fuori dei due cicli *for* nidificati si trova la struttura condizionale responsabile dell’aggiornamento del foglio di calcolo, che avviene ogni 1800 secondi (cicli while) all’interno della simulazione. L’aggiornamento del foglio di calcolo avviene tramite una funzione dello script *gSheetsManager*.

CODE

Al di fuori del ciclo while si trovano i comandi per terminare la connessione TraCI e la simulazione.

CODE

Al di fuori della funzione *run()* si trova il main, che avvierà o meno la gui a seconda delle opzioni ed assocerà alla simulazione il file *osm.sumocfg* il quale conterrà i file da importare nella simulazione. Dopo il lancio della simulazione verrà chiamata la funzione *run()*.

### File support.py

CODE

- *getDistance(mainBusPos, otherBusPos)*: la funzione calcolerà la distanza tra i due autobus usando la formula della distanza tra 2 punti;
- *inList(bus, connectedBusList)*: verifica la presenza o meno dell’autobus principale all’interno di una lista;
- *inDictionary(bus, connectedBusList)*: controlla se nel dizionario è presente l’elemento passato, ovvero l’autobus secondario.

### File gSeetsManager.py
Il file è responsabile della connessione con le API di google sheet e l’aggiornamento del foglio di calcolo collegato.

CODE

Lo script inizialmente instaura una connessione con il foglio di calcolo e cancellerà le celle riempite da dati di simulazioni precedenti. 
Nello script sono presenti 2 funzioni:
- *next_aviable_row(worksheet)*: la funzione restituirà un intero con il numero della prima riga vuota;
- *updateSheet(busList*): la funzione raggrupperà il range di valori da aggiornare e con un’unica chiamata alle API aggiornerà il foglio di calcolo nel range di valori corrispondente a *busList*.

### File  osm.sumocfg
Attraverso questo file è possibile configurare la simulazione impostando file addizionali in accordo con la [documentazione](https://sumo.dlr.de/docs/Simulation/Basic_Definition.html#input_files) 

CODE

I file che abbiamo impiegato in input nella simulazione sono, osm.net.xml che contiene la rete stradale della città di trento. Come file addizionali invece: *pt_vtypes.xml* che contiene la tipologia di veicoli impiegati nella simulazione, *gtfs_publictransport.add.xml* contenente la lista di fermate ed i percorsi che gli autobus effettueranno durante la simulazione ed infine *gtfs_publictransport.rou.xml* il quale è responsabile del percorso che gli autobus devono seguire.


































