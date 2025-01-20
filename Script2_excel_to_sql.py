# INIZIO SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE
# Importa il file di configurazione parametri constants.py
import constants

# Importa le librerie
import sqlite3  # libreria per la gestione del database SQLite
import pandas   # libreria per la gestione dei file excel
# FINE SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE

# Funzione per leggere i dati dal file Excel
def leggi_dati_excel(file_name):
    try:
        df = pandas.read_excel(file_name)
        return df
    except Exception as e:
        print(f"Errore nel leggere il file Excel: {e}")
        return None

# Funzione per creare la connessione al database
def crea_connessione_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Errore nella connessione al database: {e}")
        return None

# Funzione per creare la tabella nel database, se non esiste
def crea_tabella(cursor):
    try:
        cursor.execute('''
        CREATE TABLE canditati (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cognome TEXT,
            email TEXT,
            telefono TEXT,
            identificativo TEXT
        )
        ''')
    except sqlite3.Error as e:
        print(f"Errore nella creazione della tabella: {e}")

# Funzione per inserire i dati nella tabella
def inserisci_dati(cursor, df):
    try:
        for _, row in df.iterrows():
            cursor.execute('''
            INSERT INTO canditati (nome, cognome, email, telefono, identificativo) 
            VALUES (?, ?, ?, ?, ?)
            ''', (row['Nome'], row['Cognome'], row['Email'], row['Telefono'], row['Identificativo']))
    except sqlite3.Error as e:
        print(f"Errore nell'inserimento dei dati: {e}")

# Funzione per leggere e stampare i dati dalla tabella
def leggi_e_stampa_dati(cursor):
    try:
        cursor.execute("SELECT * FROM canditati")
        for row in cursor.fetchall():
            print(row)
    except sqlite3.Error as e:
        print(f"Errore nella lettura dei dati: {e}")

# Funzione principale per eseguire tutto il processo
def main():
    try:
        # Legge i dati dal file Excel
        df = leggi_dati_excel(constants.EXCEL_FILE_NAME)
        if df is None:
            return  # Esce dalla funzione se non è stato possibile caricare il file Excel

        # Crea una connessione al database
        conn = crea_connessione_db(constants.DB_FILE_NAME)
        if conn is None:
            return  # Esce dalla funzione se non è stato possibile connettersi al database

        cursor = conn.cursor()

        # Crea la tabella se non esiste
        crea_tabella(cursor)

        # Inserisce i dati nella tabella
        inserisci_dati(cursor, df)

        # Salva i dati nel db
        conn.commit()

        # Verifica i dati inseriti
        print("\nDati presenti nel database:")
        leggi_e_stampa_dati(cursor)

    except Exception as e:
        print(f"Errore durante l'esecuzione del programma: {e}")

    finally:
        # Assicurati che la connessione venga chiusa, anche in caso di errore
        if 'conn' in locals():
            conn.close()
            print("\nConnessione al database chiusa.")

    # Conferma che i dati sono stati inseriti correttamente
    print("\nDati inseriti nel database SQL \"" + str(constants.DB_FILE_NAME) + "\" con successo!")

# Esegui il main program solo se lo script è stato eseguito direttamente e non importato come modulo per eseguire le altre funzioni contenuto nello script 
if __name__ == "__main__":
    main()
