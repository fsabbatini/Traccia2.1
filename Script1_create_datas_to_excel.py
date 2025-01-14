# INIZIO SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE
# Importa il file di configurazione parametri constants.py
import constants

# Importa le librerie
import pandas   # libreria per la gestione dei file excel
from faker import Faker # libreria per la creazione di dati casuali

# Funzione per inizializzare l'oggetto Faker con la localizzazione da constants
def init_faker():
    try:
        fake_data = Faker(constants.FAKER_LOCALIZATION)
        return fake_data
    except Exception as e:
        print(f"Errore durante l'inizializzazione di Faker: {e}")
        raise  # Rilancia l'eccezione per interrompere l'esecuzione se necessario

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
        raise  # Rilancia l'eccezione per interrompere l'esecuzione se necessario

# Funzione per creare il DataFrame e salvarlo in un file Excel
def save_to_excel(user_data):
    try:
        df = pandas.DataFrame(user_data)
        df.to_excel(constants.EXCEL_FILE_NAME, index=False)
    except FileNotFoundError as fnf_error:
        print(f"Errore nel salvataggio del file Excel: {fnf_error}")
        raise  # Rilancia l'eccezione per interrompere l'esecuzione se necessario
    except Exception as e:
        print(f"Errore durante il salvataggio del file Excel: {e}")
        raise  # Rilancia l'eccezione per interrompere l'esecuzione se necessario

# Funzione principale per eseguire l'intero processo
def main():
    try:
        # Inizializza Faker
        fake_data = init_faker()

        # Genera i dati degli utenti
        user_data = generate_user_data(fake_data, constants.ROW_NUMBERS)

        # Salva i dati in un file Excel
        save_to_excel(user_data)

        print()
        print(f"File Excel \"{constants.EXCEL_FILE_NAME}\" creato con successo!")
    
    except Exception as e:
        print(f"Si è verificato un errore durante l'esecuzione del programma: {e}")

# Esegui il programma
if __name__ == "__main__":
    main()
