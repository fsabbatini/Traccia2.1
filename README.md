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
- "README.md" (il presente file)
- "parameters.py"
- "Script1_create_data_to_excel_class.py"
- "Script2_excel_to_sql_to_verify_class.py"

Il file "paramaters.py" contiene solo variabili di configurazione utili agli script principali

Il comando per eseguire il primo script è:
> python3 Script1_create_data_to_excel_class.py
che come output, se non ci sono stati errori, produrrà il seguente messaggio:
- "File Excel "elenco_canditati.xlsx" creato con successo, eseguire lo script successivo".
In caso di errori verrà stampato il messaggio di errore corrispondente al punto di interruzione dello script.
A questo punto la cartella di sistema dal quale si è lanciato lo script conterrà il nuovo file Excel file "elenco_candidati.xlsx", come sotto:
<img width="444" alt="Screenshot 2025-01-25 alle 14 45 00" src="https://github.com/user-attachments/assets/3cb7dd2e-4341-4fe3-a40b-34ac3ad31986" />



Il secondo file da eseguire è "Script2_excel_to_sql_to_verify_class.py" con il comando:
> python3 Script2_excel_to_sql_to_verify_class.py
Questo script leggerà i dati dal file "elenco_candidati.xlsx" e inserirà tali dati in un database SQLite, denominato "canditati.db", dopo averlo creato.

Se i due script sono stati eseguiti in successione, nella stessa cartella dovrebbero ora trovarsi due ulteriori file "elenco_candidati.xlsx" e "canditati.db". 

In caso di errori verrà stampato il messaggio di errore corrispondente al punto di interruzione dello script, altrimenti verranno stampati a video i dati del file Excel e quelli presenti nel database, formattati allo stesso modo, per facilitare un veloce confronto degli stessi, come sotto:
<img width="713" alt="Screenshot 2025-01-25 alle 14 57 51" src="https://github.com/user-attachments/assets/9cc87a38-142a-48ac-b2c4-2c69680ef7fc" />



I dati all'interno del database possono essere letti con un qualsiasi programma di gestione DB (come, ad esempio DBbrowser SQLite scaricabile dal sito https://sqlitebrowser.org
