import constants
import pandas
from faker import Faker
import random
import string

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
                    "Identificativo": ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
                }
                user_data.append(user)
            return user_data
        except Exception as e:
            print(f"Errore durante la generazione dei dati degli utenti: {e}")


def save_to_excel(user_data, file_name):
        try:
            # Crea un DataFrame dai dati degli utenti e lo salva in un file Excel
            df = pandas.DataFrame(user_data)
            df.to_excel(file_name, index=False)
        except Exception as e:
            print(f"Errore durante il salvataggio del file Excel: {e}")

def main():
    try:
        # Inizializza l'oggetto UserDataGenerator con la localizzazione
        user_data_generator = UserDataGenerator(constants.FAKER_LOCALIZATION)

        # Genera dati casuali per il numero di utenti definito in constants.py
        user_data = user_data_generator.generate_user_data(constants.HOW_MANY_USERS)

        # Salva i dati degli utenti in un file Excel
        save_to_excel(user_data, constants.EXCEL_FILE_NAME)

        print(f"\nFile Excel \"{constants.EXCEL_FILE_NAME}\" creato con successo, eseguire lo script successivo")
    
    except Exception as e:
        print(f"Si è verificato un errore durante l'esecuzione del programma: {e}")

if __name__ == "__main__":
    main()