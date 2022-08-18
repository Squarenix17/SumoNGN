# Progetto SUMO
## Next Generation Networks 

Docente del corso:

Fabrizio Granelli 


**Yousef Soliman Mekheimar - Gabriele Ughetto**


# Introduzione

![app](/images/app.png)

<div style="text-align: justify">Il progetto realizzato permette di ottenere un riscontro sulle interconnessioni degli autobus della città di Trento, fornisce il numero di incroci, l’orario di incrocio e il tempo di connessione tra due bus che si incrociano in un area di diametro 20 metri.

![bus](/images/bus.png)


La struttura del progetto si può suddividere in quattro fasi:
Setting e requisiti di Network iniziali 
Ricerca e mappatura dati GTFS sul Network
Elaborazione dei dati con Python e TraCI
Esportazione dei risultati su Google Sheet

![struttura](/images/struttura.png)



# Tutorial Progetto SUMO - Come Avviare la Simulazione
Introduzione:
Una volta clonata la repository nel proprio computer è possibile lanciare la simulazione presente nel progetto, realizzata in python, avviando il file runner.py presente nella cartella, una volta che sono soddisfatti i requisiti necessari.
### Requisiti:
Per avviare la simulazione sopracitata è necessario rispettare i seguenti requisiti:
- Sumo (https://sumo.dlr.de/docs/Installing/index.html)
- Python 3.X (https://www.python.org/downloads/)
- Tool di python necessari: Pandas, gspread 
- Account Developer su Google (https://developers.google.com/)

### Procedura:
Installare SUMO seguendo dettagliatamente la documentazione, facendo attenzione ad impostare correttamente i path nelle variabili di sistema. 

Su Windows sconsigliamo di installare SUMO nelle Cartelle Program Files o Program Files(x86) poiché possono esserci dei conflitti se vengono avviate simulazioni senza permessi di amministratore. Installando SUMO ad esempio nella cartella utente non si presentano queste problematiche.
IMPORTANTE alle variabili di sistema è necessario aggiungere "/your/path/to/sumo/tools"      PYTHONPATH
Installare Python ed i moduli utilizzando PIP, il package installer di Python per la versione che si intende utilizzare per lanciare la simulazione.

Dalla console per sviluppatori di google (https://console.developers.google.com/) è necessario creare un nuovo progetto, cliccando nel menù a tendina a destra della scritta Google Cloud

![screen1](/images/screen1.png)
![screen2](/images/screen2.png)

Creare un progetto:

![](/images/screen3.png)

Una volta nella dashboard del  progetto, cercare nella barra di ricerca: Google Sheets API
![](/images/screen4.png)
![](/images/screen5.png)

Ed abilitare le API, fare la stessa cosa per le API di Google Drive
![](/images/screen6.png)

Recandosi nella dashboard selezionare Service Accounts
![](/images/screen7.png)

E creare un nuovo service account
![](/images/screen8.png)
![](/images/screen9.png)

premere create and continue e selezionare il ruolo Editor:

![](/images/screen10.png)

Una volta creato cliccare l’email del Service Account

![](/images/screen11.png)

Recandosi in Keys

![](/images/screen12.png)

è necessario creare una nuova chiave privata in json:

![](/images/screen13.png)

Questo file andrà rinominato in token.json ed inserito nella cartella del programma.

![](/images/screen14.png)


Ora sarà necessario creare il foglio di calcolo su Google docs, il quale è importante che venga rinominato Sumo Data (Con nomi differenti la simulazione non funzionerà), noi consigliamo semplicemente di creare una copia del file da noi creato: Sumo Data 

Nella copia del file Sumo Data è importante condividere l’accesso con la mail del Service Account creato in precedenza: 

![](/images/screen15.png)


Se sono stati eseguiti tutti i passaggi correttamente è ora possibile lanciare la simulazione utilizzando il file runner.py 

![](/images/screen16.png)

Si aprirà in automatico il file Google Sheet Sumo Data

![](/images/screen17.png)

e per far partire la simulazione sarà necessario premere sulla freccia verde Run

![](/images/screen18.png)

per velocizzare la simulazione suggeriamo di ridurre il Delay a 0 e impostare la visualizzazione della mappa in faster standard

![](/images/screen19.png)

si apre anche la finestra dello script python che contiene:
Orario
Numero bus presenti sulla mappa
Numero di bus connessi tra loro

![](/images/screen20.png)

e man mano che il programma rileva le connessioni tra i bus le trascriverà sul file Google Sheet indicando 
Nome del bus principale
Nome del bus che viene incontrato
Tempo per il quale rimangono connessi
Orario in cui avviene l’incrocio

![](/images/screen21.png)

L’aggiornamento sul foglio di calcolo avviene ogni 1800 secondi (30 minuti) trascorsi all’interno della simulazione.</div>

# Tutorial Progetto SUMO - Come Ricreare la Simulazione
La creazione della simulazione PT consiste in tre fasi:
- Requisiti di rete iniziali (OSM)
- Trovare un'origine dati per GTFS
- Mappatura dei dati GTFS sulla rete
- OSM Web Wizard
