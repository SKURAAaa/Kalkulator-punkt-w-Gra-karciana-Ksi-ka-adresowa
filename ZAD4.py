import random


class Karta:
    def __init__(self, kolor, figura, punkty):
        self.kolor = kolor
        self.figura = figura
        self.punkty = punkty

    def __str__(self):
        return f"{self.figura} {self.kolor} ({self.punkty} punktów)"


def generuj_talie():
    kolory = ["Kier", "Karo", "Trefl", "Pik"]
    figury = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Walet": 11, "Dama": 12, "Król": 13, "As": 14
    }
    talia = []
    for kolor in kolory:
        for figura, punkty in figury.items():
            talia.append(Karta(kolor, figura, punkty))
    return talia


def graj(talia):
    gracz1_punkty = 0
    gracz2_punkty = 0
    random.shuffle(talia)

    for _ in range(5):  # graj 5 rund
        input("Naciśnij Enter, aby przeprowadzić atak...")  # Sygnał do ataku
        karta1 = talia.pop()
        karta2 = talia.pop()

        print(f"Gracz 1: {karta1}")
        print(f"Gracz 2: {karta2}")

        if karta1.punkty > karta2.punkty:
            gracz1_punkty += 1
            print("Gracz 1 wygrywa rundę!\n")
        elif karta1.punkty < karta2.punkty:
            gracz2_punkty += 1
            print("Gracz 2 wygrywa rundę!\n")
        else:
            print("Remis!\n")

    print(f"Końcowy wynik: Gracz 1: {gracz1_punkty} - Gracz 2: {gracz2_punkty}")
    if gracz1_punkty > gracz2_punkty:
        print("Gracz 1 wygrywa grę!")
    elif gracz1_punkty < gracz2_punkty:
        print("Gracz 2 wygrywa grę!")
    else:
        print("Gra kończy się remisem!")


# Generowanie talii i start gry
talia = generuj_talie()
graj(talia)


# Zad 4. Gra karciana
# Stwórz klasę Karta, która będzie miała atrybuty: kolor, figura, punkty. Gdzie np “2”, będzie
# miało 2 punkty, “Walet” będzie miał 11, “Królowa” 12 itd. Wygeneruj instancje kart
# reprezentujące pełną talię do gry. Następnie przy pomocy konsoli losuj dwie karty, które
# będą walczyły. W zależności od wyniku dopisuj punkt dla “gracz 1”, “gracz 2”. Niech “atak”
# odbywa się po wysłaniu losowego sygnału do konsoli.
