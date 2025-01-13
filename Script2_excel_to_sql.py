# INIZIO SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE
# Importa il file di configurazione parametri constants.py
import constants

# Importa le librerie
import sqlite3  # libreria per la gestione del database SQLite
import pandas   # libreria per la gestione dei file excel
# FINE SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE

# Legge i dati dal file Excel creato dallo Script1 in una variabile dataframe
df = pandas.read_excel(constants.EXCEL_FILE_NAME)

# Crea una connessione al database SQLite (se non esiste verrà creato un file .db)
conn = sqlite3.connect(constants.DB_FILE_NAME)
cursor = conn.cursor()

# Se non esiste crea la tabella SQL
cursor.execute('''
CREATE TABLE IF NOT EXISTS canditati (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cognome TEXT,
    email TEXT,
    telefono TEXT
)
''')

# Inserisce i dati nella tabella SQL
for _, row in df.iterrows():
    cursor.execute('''
    INSERT INTO canditati (nome, cognome, email, telefono) 
    VALUES (?, ?, ?, ?)
    ''', (row['Nome'], row['Cognome'], row['Email'], row['Telefono']))

# Salva i dati nel db
conn.commit()

# Verifica i dati inseriti eseguendo la query SQL per leggere l'intera tabella e stamparla a video riga x riga
cursor.execute("SELECT * FROM canditati")
print()
for row in cursor.fetchall():
    print(row)

# Chiudi la connessione al db
conn.close()

print()
print("Dati inseriti nel database SQL \"" + str(constants.DB_FILE_NAME) + "\" con successo!")
