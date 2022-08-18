## Problematiche

Durante il progetto abbiamo riscontrato alcune problematiche.

### **Mappa con connessioni imprecise o interrotte**
Il tool fornito da SUMO osmWebWizard, che consente di selezionare una regione geografica su Open Street Map e convertirla in una rete pronta per essere simulata, presenta delle problematiche per aree molto grandi. Abbiamo tentato gli altri metodi consigliati nella sezione [OSM](https://sumo.dlr.de/docs/Tools/Import/OSM.html) della documentazione, ma la problematica persisteva. La mappa dunque rappresentata non è totalmente fedele a quella della città di Trento e alcuni percorsi degli autobus potrebbero averne risentito con la conseguenza che il percorso simulato non rappresenterà quello reale in alcune zone.

### **Simulazione pesante** 
La simulazione deve coprire una zona molto vasta con numerose intersezioni, infatti nelle ore in cui sono presenti più autobus, dalle 7:00 alle 16:00 circa, il tempo di computazione che richiede ogni ciclo aumenta in maniera significativa. Al fine di non rendere ulteriormente pensante la simulazione abbiamo deciso di non implementare un traffico generato randomicamente.

### **Modifica del file *gtfs_publictransport.rou.xml***
Il file gtfs_publictransport.rou.xml ottenuto dallo script *gtfs2pt.py* utilizzando il GTFS fornito da Trentino Trasporti presentava un id degli autobus poco riconoscibile, pertanto abbiamo modificato manualmente l’id di ogni bus nel seguente modo:

vehicle id="lNumeroLinea_dOrarioPartenza_rNumeroRoute"

### **Aggiornamento API** 
Durante la simulazione l’aggiornamento del foglio di calcolo non avviene ad ogni ciclo, le motivazioni di questa scelta sono due, la prima è il limite di richieste al minuto delle api google, le quali non permettono di stare al passo con l’esecuzione della simulazione. La seconda motivazione riguarda la velocità con cui viene eseguita la richiesta, TraCI infatti prima di proseguire al ciclo successivo attenderà l’avvenuta scrittura nel foglio di calcolo e il tempo di attesa per ogni chiamata è significativo. La chiamata alle API sarà eseguita una sola volta raggruppando tutte le celle da aggiornare.