# Traccia2.1
 
# Project Work Università Telematica "UniPegaso"

## Introduzione

Repository contenente gli elaborati in merito alla Tesi del Corso di Laurea L-31 "Informatica per le Aziende Digitali".
La traccia scelta è la 2.1: "Ruolo della privacy e sull'importanza del GDPR".

Il progetto, relativamente alla parte tecnica, richiede lo sviluppo di due script Python con i seguenti obiettivi:
- Il primo script deve generare dati casuali per 10 persone (nome, cognome, e-mail, numero di telefono), salvando tali dati in un file di tipo Excel
- Il secondo script deve recuperare i dati dal file Excel creato dallo script precedente e creare un database, utilizzando il linguaggio SQL, con relativa tabella,  ed inserire i dati così recuperati al suo interno, assicurandosi, tramite stampa a video, che i dati contenuti nel file Excel e la tabella del database corrispondano
  
NB: agli obiettivi base del progetto sono state effettuate le seguenti implementazioni:
- Campo "idenditificativo" univoco
- File "Parameters.py" per la configurazione di base di entrambi gli script realizzati

## Prerequisiti

Per il corretto funzionamento degli script, è necessario installare i seguenti software:
- interprete Python (può essere scaricato per tutti i comuni sistemi operativi dal sito ufficiale: https://www.python.org/downloads/)
- modulo Faker (https://github.com/joke2k/faker)
- da terminale, spostarsi in una cartella a scelta per scaricare i file di progetto, contenuti nella cartella Traccia2.1, tramite il seguente comando:
> git clone https://github.com/fsabbatini/Traccia2.1
In alternativa al comando git clone, è possibile scaricare l'intero progetto in formato .zip, ed estrarlo una volta completato il download. Per far ciò, è necessario cliccare sul tasto "Code" in alto, e nel menu che si apre selezionare "Download zip".

## Installazione Faker

Faker è un package Python per la generazione casuale di dati, semplice da utilizzare e da configurare. E' stata scelta per questo progetto perché permette una localizzazione dei dati e la selezione tra un ampio range di dati disponibili, coprendo ampiamente i requisiti richiesti dal progetto.

Per installarlo, basta aprire il terminale ed eseguire il seguente comando:
> pip install faker

Infine è necessario che gli script siano contenuti tutti nella stessa cartella, in modo che gli output possano essere recuperati correttamente dai vari script.
Clonare o scaricare questo progetto è condizione sufficiente per poter eseguire gli script senza problemi.

## Esecuzione

Per poter eseguire correttamente gli scripts, aprire il terminale del proprio SO di riferimento, e spostarsi all'interno della cartella clonata di questo progetto, contenente tutti i file necessari.

Dopodiché, andranno eseguiti gli script tramite il comando generico:
> python3 <NOME_SCRIPT>.py
Nel caso si ricevesse un errore relativamente al comando verificare che il path del comando pyhton3 sia corrispondente

All'interno della cartella è possibile trovare:
- `README.md` (il presente file)
- `parameters.py`
- `Script1_create_data_to_excel_class.py`
- `Script2_excel_to_sql_to_verify_class.py`

Il file `paramaters.py` contiene solo variabili di configurazione utili agli Script

Il comando per eseguire il primo script è:
> python3 Script1_create_data_to_excel_class.py
che come output, se non ci sono stati errori, produrrà il seguente messaggio:
- "File Excel "elenco_canditati.xlsx" creato con successo, eseguire lo script successivo".
In caso di errori verrà stampato il messaggio di errore corrispondente al punto di interruzione dello script.
A questo punto la cartella di sistema dal quale si è lanciato lo script conterrà il nuovo file Excel file "elenco_candidati.xlsx", vedere esempio:

Nome	     Cognome	  Email	                       Telefono	      Identificativo
Vittorio	 Gualtieri	arsenioiannuzzi@example.org	 0813871149	    A0D2E
Tonino    Palladio	 ebova@example.org	           +39 0544039728	14975
Nico	     Foletti	  annibale59@example.org	      +39 042992907	 D400B
Biagio	   Abba	     isabellafagiani@example.net	 +39 042184477	 6258C
Biagio	   Visconti	 bbova@example.net	           377629460	     ECBF5
Daniele	  Monicelli	nicolettamannoia@example.org	+39 3534117616	9E9FD
Daria	    Tiepolo	  fedelecurci@example.com	     +39 3713683831	CA631
Severino	 Antonucci	trezzinitorquato@example.com	0123481690	    4AB5D
Napoleone Zanazzo	  vmuratori@example.net	       +39 3514415443	3C3FC
Graziano	 Faranda	  gianluigi24@example.net	     35113552547	   8FE9E
<img width="444" alt="Screenshot 2025-01-25 alle 14 42 36" src="https://github.com/user-attachments/assets/4c2506b8-43ae-4872-8da8-a3079d2bc8e1" />

Il secondo file da eseguire è `Script2_excel_to_sql_to_verify_class.py`. Questo script cercherà nella stessa cartella un file "elenco_candidati.xlsx" e, se lo troverà, proverà ad inserire tali dati in un database SQLite, dopo averlo creato.
In questo secondo script vengono prese diverse misure per verificare la validità dei dati recuperati dal file `people_data.csv` (come, ad esempio, fermare l'esecuzione del codice se il file non esiste, oppure è vuoto, o se i dati non sono formattati correttamente). 

Se i due script `first_script.py` e `second_script.py` sono stati eseguiti in successione, nella stessa cartella dovrebbero ora trovarsi due ulteriori file `people_data.csv` e `people_data.db`. 

I dati all'interno del database possono essere letti con un qualsiasi programma di gestione DB (come, ad esempio DBeaver).

Lo script `second_script.py` una volta creata la tabella 'people' (se non presente) ed aver inserito i dati recuperati dal file `people_data.csv` (dopo aver eliminato i precedenti), effettua un check di validazione tra i dati contenuti in `people_data.csv` e quelli in `people_data.db`. Il confronto tra i dati viene effettuato dopo aver ordinato le relative righe di entrambi i file in modo che il confronto sia position-insensitive. Ottenuto tale risultato, esso viene mostrato all'interno del terminale.
