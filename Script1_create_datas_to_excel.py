# INIZIO SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE
# Importa il file di configurazione parametri constants.py
import constants

# Importa le librerie
import pandas   # libreria per la gestione dei file excel
from faker import Faker # libretia per la creazione di dati casuali

# Inizializza l'oggetto Faker e per comodità di lettura/verifica dati attiviamo la localizzazione definita nel file constants
fake_data = Faker(constants.FAKER_LOCALIZATION)

# Crea una lista di dizionari con i dati degli utenti, tanti quanti definiti in constants.ROW_NUMBERS
user_data = []
for _ in range(constants.ROW_NUMBERS):
    user = {
        "Nome": fake_data.first_name(),
        "Cognome": fake_data.last_name(),
        "Email": fake_data.email(),
        "Telefono": fake_data.phone_number()
    }
    user_data.append(user)

# Crea un DataFrame dalla lista di dizionari
df = pandas.DataFrame(user_data)

# Salva i dati in un file Excel con nome definito in constants.EXCEL_FILE_NAME
df.to_excel(constants.EXCEL_FILE_NAME, index=False)

print()
print("File Excel \"" + str(constants.EXCEL_FILE_NAME) + "\" creato con successo!")

