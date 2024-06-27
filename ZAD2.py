from ZAD1 import Pojazd


class Autobus(Pojazd):
    def __init__(self, predkosc_max, przebieg, model, ilosc_siedzen):
        super().__init__(predkosc_max, przebieg)
        self.model = model
        self.ilosc_siedzen = ilosc_siedzen


# instancjA klasy Autobus
autobus1 = Autobus(100, 50000, "Mercedes", 50)

print("Maksymalna prędkość:", autobus1.predkosc_max)
print("Przebieg:", autobus1.przebieg)
print("Model:", autobus1.model)
print("Ilość siedzeń:", autobus1.ilosc_siedzen)


# Zad 2. Stwórz klasę Autobus, która dziedziczy po Pojazd utworzonym wcześniej, ale do
# atrybutów pojazdu dodaj jeszcze nazwę modelu. Do Autobus dodaj atrybut ilosc_siedzen.
# Stwórz instancję tej klasy i wydrukuj jej atrybuty.