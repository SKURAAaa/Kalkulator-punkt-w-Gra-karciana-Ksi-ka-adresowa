class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def srednia(self):
        return sum(self.oceny) / len(self.oceny) if self.oceny else 0

    def dodaj_ocene(self, ocena):
        if isinstance(ocena, (int, float)) and 0 <= ocena <= 5:
            self.oceny.append(ocena)
        else:
            raise ValueError("Ocena musi być liczbą od 0 do 5.")

    def __add__(self, ocena):
        self.dodaj_ocene(ocena)
        return self

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, średnia ocen: {self.srednia():.2f}"

# Tworzenie instancji klasy Student
student1 = Student("Jan", "Kowalski")
student1.dodaj_ocene(4)
student1.dodaj_ocene(5)
student1 += 3

# Wydruk opisu instancji
print(student1)




# Zad 3. Kalkulator punktów.
# Stwórz klasę Student, która będzie przechowywać listę ocen studenta. Dodaj metodę
# srednia, która oblicza średnią ocen studenta na podstawie listy ocen. Dodaj również metodę
# dodaj_ocene(ocena), która pozwala dodawać oceny do listy.Dodatkowo, zaimplementuj
# przeciążenie operatora + dla studenta, która będzie dodawała dodatkową ocenę do listy.
# Przesłoń również metodę zwracającą opis instancji obiektu. Niech zwraca imię, nazwisko i
# średnią ocen. Dodaj podstawową obsługę błędów, tj typ zmiennej, zakres ocen itp.