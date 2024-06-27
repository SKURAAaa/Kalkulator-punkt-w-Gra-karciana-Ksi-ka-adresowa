class Pojazd:
    def __init__(self, predkosc_max, przebieg):
        self.predkosc_max = predkosc_max
        self.przebieg = przebieg

# Tworzenie instancji klasy Pojazd
pojazd1 = Pojazd(150, 12000)

# Wydruk atrybutów instancji
print("Maksymalna prędkość:", pojazd1.predkosc_max)
print("Przebieg:", pojazd1.przebieg)






# Zad 1. Stwórz klasę “Pojazd” z atrybutami predkosc_max i przebieg. Stwórz instancję klasy i
# wydrukuj jej atrybuty do konsoli. Tworząc instancję można podać dowolne wielkości.