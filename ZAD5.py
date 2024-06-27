import json

class Kontakt:
    def __init__(self, imie, nazwisko, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def __str__(self):
        return f"{self.imie} {self.nazwisko}: {self.telefon}"

    def to_dict(self):
        return {'imie': self.imie, 'nazwisko': self.nazwisko, 'telefon': self.telefon}

    @classmethod
    def from_dict(cls, data):
        return cls(data['imie'], data['nazwisko'], data['telefon'])

class KsiazkaAdresowa:
    def __init__(self):
        self.kontakty = []

    def dodaj_kontakt(self, kontakt):
        self.kontakty.append(kontakt)

    def usun_kontakt(self, nazwisko):
        self.kontakty = [kontakt for kontakt in self.kontakty if kontakt.nazwisko != nazwisko]

    def wyswietl_kontakty(self):
        for kontakt in self.kontakty:
            print(kontakt)

    def wyswietl_kontakt(self, nazwisko):
        for kontakt in self.kontakty:
            if kontakt.nazwisko == nazwisko:
                print(kontakt)
                return
        print(f"Kontakt z nazwiskiem {nazwisko} nie został znaleziony.")

    def zapisz_do_pliku_json(self, nazwa_pliku):
        with open(nazwa_pliku, 'w') as plik:
            json.dump([kontakt.to_dict() for kontakt in self.kontakty], plik)

    def wczytaj_z_pliku_json(self, nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            self.kontakty = [Kontakt.from_dict(data) for data in json.load(plik)]

# Interfejs użytkownika
def main():
    ksiazka = KsiazkaAdresowa()

    while True:
        print("\nMenu:")
        print("1. Dodaj kontakt")
        print("2. Usuń kontakt")
        print("3. Wyświetl wszystkie kontakty")
        print("4. Wyświetl pojedynczy kontakt")
        print("5. Zapisz do pliku")
        print("6. Wczytaj z pliku")
        print("7. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            telefon = input("Podaj telefon: ")
            kontakt = Kontakt(imie, nazwisko, telefon)
            ksiazka.dodaj_kontakt(kontakt)
            print("Dodano kontakt.")

        elif wybor == '2':
            nazwisko = input("Podaj nazwisko kontaktu do usunięcia: ")
            ksiazka.usun_kontakt(nazwisko)
            print("Usunięto kontakt.")

        elif wybor == '3':
            print("Wszystkie kontakty:")
            ksiazka.wyswietl_kontakty()

        elif wybor == '4':
            nazwisko = input("Podaj nazwisko kontaktu do wyświetlenia: ")
            ksiazka.wyswietl_kontakt(nazwisko)

        elif wybor == '5':
            nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
            ksiazka.zapisz_do_pliku_json(nazwa_pliku)
            print("Zapisano kontakty do pliku.")

        elif wybor == '6':
            nazwa_pliku = input("Podaj nazwę pliku do wczytania: ")
            ksiazka.wczytaj_z_pliku_json(nazwa_pliku)
            print("Wczytano kontakty z pliku.")

        elif wybor == '7':
            break

        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

if __name__ == "__main__":
    main()



# Zad 5. Książka adresowa
# Stwórz program do przechowywania listy kontaktów. Stwórz klasę Kontakt, reprezentującą
# pojedynczy wpis i KsiązkaAdresowa reprezentującą listę wszystkich instancji klasy Kontakt.
# Niech książka adresowa ma możliwość dodawania kontaktu, usuwania, wyświetlenia
# wszystkich i wyświetlania pojedynczego kontaktu.
# Dodatkowo dodaj serializację, która pozwoli na zapis ksiażki i odczyt z pliku.
# Może to być przy pomocy pickle