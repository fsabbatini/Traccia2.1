# INIZIO SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE
# Importa il file di configurazione parametri constants.py
import constants

# Importa le librerie
import pandas   # libreria per la gestione dei file excel
from faker import Faker # libreria per la creazione di dati casuali

# Funzione per inizializzare l'oggetto Faker con la localizzazione definita in constants
def init_faker():
    try:
        fake_data = Faker(constants.FAKER_LOCALIZATION)
        return fake_data
    except Exception as e:
        print(f"Errore durante l'inizializzazione di Faker: {e}")

# Funzione per generare una lista di dizionari con i dati degli utenti
def generate_user_data(fake_data, num_users):
    try:
        user_data = []
        for _ in range(num_users):
            user = {
                "Nome": fake_data.first_name(),
                "Cognome": fake_data.last_name(),
                "Email": fake_data.email(),
                "Telefono": fake_data.phone_number()
            }
            user_data.append(user)
        return user_data
    except Exception as e:
        print(f"Errore durante la generazione dei dati degli utenti: {e}")

# Funzione per creare il DataFrame e salvarlo in un file Excel
def save_to_excel(user_data):
    try:
        df = pandas.DataFrame(user_data)
        df.to_excel(constants.EXCEL_FILE_NAME, index=False)
    except Exception as e:
        print(f"Errore durante il salvataggio del file Excel: {e}")

# Funzione principale (Main program) 
def main():
    try:
        # Inizializza Faker con la localizzazione
        fake_data = init_faker()

        # Genera i dati casuali di n. 10 utenti
        user_data = generate_user_data(fake_data, constants.ROW_NUMBERS)

        # Salva i dati in un file Excel
        save_to_excel(user_data)

        print(f"\nFile Excel \"{constants.EXCEL_FILE_NAME}\" creato con successo, eseguire lo script successivo")
    
    except Exception as e:
        print(f"Si è verificato un errore durante l'esecuzione del programma: {e}")

# Esegui il main program solo se lo script è stato eseguito direttamente e non importato come modulo per eseguire le altre funzioni contenuto nello script 
if __name__ == "__main__":
    main()
