# INIZIO SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE
import Parameters    # Importa il file di configurazione parametri parameters.py

# Importa le librerie
import pandas           # libreria per la gestione dei file excel
from faker import Faker # libreria per la creazione di dati casuali    
import string           # libreria per la gestione delle stringhe
import uuid             # libreria per la generazione di codici identificatori univoci universali 
# FINE SEZIONE IMPORTAZIONE LIBRERIE/FILE DI CONFIGURAZIONE

# Questa classe contiene metodi per la generazione dei dati tramite Faker
class UserDataGenerator:
    def __init__(self, localization):
        # Inizializza l'oggetto Faker con la localizzazione fornita
        self.fake_data = self.init_faker(localization)

    def init_faker(self, localization):
        try:
            # Crea e restituisce un oggetto Faker con la localizzazione specificata
            fake_data = Faker(localization)
            return fake_data
        except Exception as e:
            print(f"Errore durante l'inizializzazione di Faker: {e}")

    # Questo metodo restituisce un numero di dati casuali per tanti utenti definiti num_users  
    def generate_user_data(self, num_users):
        try:
            user_data = []
            for _ in range(num_users):
                # Genera un dizionario con i dati dell'utente
                user = {
                    "Nome": self.fake_data.first_name(),
                    "Cognome": self.fake_data.last_name(),
                    "Email": self.fake_data.email(),
                    "Telefono": self.fake_data.phone_number(),
                    "Identificativo": ''.join(str.upper(uuid.uuid4().hex[:5])) # genera codice univoco di 5 cifre per pesudonimizzazione
                    
                }
                user_data.append(user)
            return user_data
        except Exception as e:
            print(f"Errore durante la generazione dei dati degli utenti: {e}")

# Questa funzione salva i dati che riceve nel file dal nome "file_name"
def save_to_excel(user_data, file_name):
        try:
            # Crea un DataFrame dai dati degli utenti e lo salva in un file Excel
            df = pandas.DataFrame(user_data)
            df.to_excel(file_name, index=False)
        except Exception as e:
            print(f"Errore durante il salvataggio del file Excel: {e}")

# Questa funzione (main program) gestisce il flusso dell'intero script1
def main():
    try:
        # Inizializza l'oggetto UserDataGenerator con la localizzazione
        user_data_generator = UserDataGenerator(Parameters.FAKER_LOCALIZATION)

        # Genera dati casuali per il numero di utenti definito in parameters.py
        user_data = user_data_generator.generate_user_data(Parameters.HOW_MANY_USERS)

        # Salva i dati degli utenti in un file Excel
        save_to_excel(user_data, Parameters.EXCEL_FILE_NAME)

        print(f"\nFile Excel \"{Parameters.EXCEL_FILE_NAME}\" creato con successo, eseguire lo script successivo")
    
    except Exception as e:
        print(f"Si è verificato un errore durante l'esecuzione del programma: {e}")

# Esegui il main program solo se lo script è stato eseguito direttamente
# Nel caso in cui questo script sia importato come modulo sarà possibile eseguire le altre funzioni in esso contenuto 
if __name__ == "__main__":
    main()