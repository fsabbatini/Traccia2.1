# INIZIO SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE
# Importa il file di configurazione parametri constants.py
import Parameters

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

# Questa classe contiene metodi per la gestione del database
class DatabaseManager:
    def __init__(self, db_name):
        self.conn = self.crea_connessione_db(db_name)
        self.cursor = self.conn.cursor() if self.conn else None

    def crea_connessione_db(self, db_name):
        try:
            conn = sqlite3.connect(db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Errore nella connessione al database: {e}")
            return None

    def crea_tabella(self):
        try:
            self.cursor.execute('''
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

    def inserisci_dati(self, df):
        try:
            for _, row in df.iterrows():
                self.cursor.execute('''
                INSERT INTO canditati (nome, cognome, email, telefono, identificativo) 
                VALUES (?, ?, ?, ?, ?)
                ''', (row['Nome'], row['Cognome'], row['Email'], row['Telefono'], row['Identificativo']))
        except sqlite3.Error as e:
            print(f"Errore nell'inserimento dei dati: {e}")

    def leggi_e_stampa_dati(self):
        try:
            self.cursor.execute("SELECT * FROM canditati")
            columns = ['','Nome', 'Cognome', 'Email', 'Telefono', 'Identificativo']
            df = pandas.DataFrame(self.cursor.fetchall(), columns=columns)
            df = df.drop('', axis=1)
            print(df)
        except sqlite3.Error as e:
            print(f"Errore nella lettura dei dati: {e}")

    def chiudi_connessione(self):
        if self.conn:
            self.conn.close()

# Questa funzione (main program) gestisce il flusso dell'intero script2
def main():
    try:
        # Legge e stampa i dati dal file Excel creato dalla Script1
        df = leggi_dati_excel(Parameters.EXCEL_FILE_NAME)
        if df is None:
            return  # Esce dalla funzione se non è stato possibile caricare il file Excel
        else:
            print("\nDati presenti nel file excel:")
            print(df.head(Parameters.HOW_MANY_USERS))

        # Crea una connessione al database
        db_manager = DatabaseManager(Parameters.DB_FILE_NAME)
        if db_manager.conn is None:
            return  # Esce dalla funzione se non è stato possibile connettersi al database

        # Crea la tabella se non esiste
        db_manager.crea_tabella()

        # Inserisce i dati nella tabella
        db_manager.inserisci_dati(df)

        # Salva i dati nel db
        db_manager.conn.commit()

        # Verifica i dati inseriti
        print("\nDati presenti nel database:")
        db_manager.leggi_e_stampa_dati()

    except Exception as e:
        print(f"Errore durante l'esecuzione del programma: {e}")

    finally:
        # Assicurati che la connessione venga chiusa, anche in caso di errore
        if 'db_manager' in locals():
            db_manager.chiudi_connessione()

    # Conferma che i dati sono stati inseriti correttamente
    print("\nDati inseriti nel database SQL \"" + str(Parameters.DB_FILE_NAME) + "\" con successo!")

# Esegui il main program solo se lo script è stato eseguito direttamente
# Nel caso in cui questo script sia importato come modulo sarà possibile eseguire le altre funzioni in esso contenuto 
if __name__ == "__main__":
    main()
