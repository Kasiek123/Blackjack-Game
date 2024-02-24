import random
from blackjack_cards import pobierz_grafike


def karty_do_blackjack():
    """
    Tworzenie talii kart dla każdego z koloru (pik, trefl, karo, kier),
    poprzez stworzenie dla każdego z nich słownika, powstałego przez
    scalenie kart (2-10) oraz figur (J, Q, K, A) za pomocą operatora union '|'
    """
    return {
        'pik': {str(v): v for v in range(2, 11)} | {'J': 10, 'Q': 10, 'K': 10, 'A': 11},
        'trefl': {str(v): v for v in range(2, 11)} | {'J': 10, 'Q': 10, 'K': 10, 'A': 11},
        'karo': {str(v): v for v in range(2, 11)} | {'J': 10, 'Q': 10, 'K': 10, 'A': 11},
        'kier': {str(v): v for v in range(2, 11)} | {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    }


def losowanie_kart(talia):
    """
    Losowanie kart na podstawie parametru (talia kart), w której
    najpierw wylosowany zostaje kolor, a następnie nazwe karty
    i jej wartosc z danego koloru.
    Po wylosowaniu, dana karta zostaje usunięta z talii, aby
    zapobiec jej ponownemu wylosowaniu w danej grze.
    """
    kolor = random.choice(list(talia.keys()))
    nazwa_karty, punkty = random.choice(list(talia[kolor].items()))
    del talia[kolor][nazwa_karty]
    return kolor, nazwa_karty, punkty


def suma_punktow(karty):
    """
    Sumowanie punktow na podstawie parametru (karty) poprzez iterację przez tuple.
    W przypadku obecności karty As i sumie punktów powyżej 21,
    od sumy odejmowane jest 10 punktów (wartość Asa = 1 punkt).
    """
    suma = sum(punkty for kolor, nazwa_karty, punkty in karty)
    karta_as = [i for i in karty if "A" in i]

    if suma > 21 and karta_as:
        for kolor, nazwa_karty, punkty in karty:
            if nazwa_karty == "A":
                suma -= 10
                if suma <= 21:
                    break

    return suma


def porownanie_wynikow(punkty_gracza, punkty_krupiera):
    """
    Porownanie wynikow na podstawie otrzymanych parametrow (punkty gracza i krupiera).
    Funkcja zwraca wartość logiczną (True) opisującą wynik porównań zdefiniowanych w słowniku
    """
    return f"Punkty krupiera: {punkty_krupiera}\nPunkty gracza: {punkty_gracza}\nWynik końcowy: { {
        punkty_gracza == punkty_krupiera: 'Remis',
        punkty_gracza > 21: 'Wygrywa krupier',
        punkty_krupiera > 21: 'Wygrywa gracz',
        punkty_krupiera == 21 and punkty_gracza != 21: 'Krupier wygrywa - BLACKJACK !!!',
        punkty_gracza == 21 and punkty_krupiera != 21: 'Gracz wygrywa - BLACKJACK !!!',
        (punkty_gracza > punkty_krupiera) and (punkty_gracza < 21): 'Wygrywa gracz',
        (punkty_gracza < punkty_krupiera) and (punkty_krupiera < 21): 'Wygrywa krupier'
    }[True]
    }"

# def porownanie_wynikow(punkty_gracza, punkty_krupiera):
#     if punkty_gracza > 21 and punkty_krupiera > 21:
#         wynik = "Wygrywa gracz"
#     elif punkty_gracza == punkty_krupiera:
#         wynik = "Remis"
#     elif punkty_krupiera == 21:
#         wynik = "Krupier wygrywa - BLACKJACK !!!"
#     elif punkty_gracza == 21:
#         wynik = "Gracz wygrywa - BLACKJACK !!!"
#     elif punkty_gracza > 21:
#         wynik = "Wygrywa krupier"
#     elif punkty_krupiera > 21:
#         wynik = "Wygrywa gracz"
#     elif punkty_gracza > punkty_krupiera:
#         wynik = "Wygrywa gracz"
#     else:
#         wynik = "Wygrywa krupier"
#
#     return f"Punkty krupiera: {punkty_krupiera}\nPunkty gracza: {punkty_gracza}\nWynik końcowy: {wynik}"


def grafika_kart(karty, karta_odkryta):
    """
    Funkcja na podstawie otrzymanych parametrow [karty, widzialnosc kart
    (karta zakryta/odkryta)], tworzy liste ulozonych obok siebie kart.
    """
    wszystkie_karty = []

    # Nazwa koloru karty zostaje zmieniona na odpowiadajacy jej symbol
    for index, (kolor, nazwa_karty, punkty) in enumerate(karty):
        znak_koloru = {
            kolor == "pik": "♠",
            kolor == "trefl": "♣",
            kolor == "karo": "♦",
            kolor == "kier": "♥"
        }

        # Warunek sprawdzajacy czy dana karta jest pierwsza lub czy jest odkryta
        if index == 0 or karta_odkryta:
            # pobieranie grafiki odkrytej karty z funkcji pobierz_grafike
            karta = pobierz_grafike(nazwa_karty, znak_koloru[True], widzialnosc_kart=True)
        else:
            # pobieranie grafiki zakrytej karty z funkcji pobierz_grafike
            karta = pobierz_grafike(nazwa_karty, znak_koloru[True], widzialnosc_kart=False)

        for i in range(len(karta)):
            # Warunek sprawdzajacy czy dlugosc listy wszystkie_karty jest mniejsza badz rowna i [0-4]
            if len(wszystkie_karty) <= i:
                # dodanie do listy wszystkie_karty elementow karty w zaleznosci od i
                wszystkie_karty.append(karta[i])
            else:
                # Kiedy warunek len(wszystkie_karty) <= i nie jest spelniony
                # Najpierw dodany zostanie pusty string, a nastepnie elementy karty w zaleznosci od i
                # (dzieki temu mozliwe jest ulozenie kart obok siebie, a nie jedna pod druga)
                wszystkie_karty[i] += " " + karta[i]

    return wszystkie_karty


def drukowanie_kart(karty_krupiera, karty_gracza):
    """
    Funkcja drukujaca karty krupiera i gracza na podstawie otrzymanych parametrow
    """
    print("Karty krupiera:")
    for i in karty_krupiera:
        print(i)

    print("Karty gracza")
    for j in karty_gracza:
        print(j)


def blackjack():
    gracz = []
    krupier = []
    talia_kart = karty_do_blackjack()

    # Losowanie 2 kart dla gracza i krupiera
    for i in range(2):
        gracz.append(losowanie_kart(talia_kart))
        krupier.append(losowanie_kart(talia_kart))

    while True:
        # Drukowanie kart krupiera (pierwsza widoczna, druga nie) oraz kart gracza (obie widoczne)
        drukowanie_kart(grafika_kart(krupier, karta_odkryta=False), grafika_kart(gracz, karta_odkryta=True))
        print(f"Aktualny wynik gracza: {suma_punktow(gracz)}")

        # Warunek sprawdzajacy czy krupier/gracz ma 21 punktow lub gracz przekroczyl 21 punktow
        if suma_punktow(krupier) == 21 or suma_punktow(gracz) == 21 or suma_punktow(gracz) > 21:
            break
        else:
            # Kiedy warunek krupier/gracz ma 21 punktow lub gracz przekroczyl 21 punktow nie jest spelniony
            # Gracz moze dobrac kolejna karte
            if input("Czy chcesz dobrac kolejna karte? (y/n) ").lower() == "y":
                gracz.append(losowanie_kart(talia_kart))
            else:
                break

    # Warunek sprawdzajacy czy wartosc kart krupiera jest mniejsza od 17
    while suma_punktow(krupier) < 17 and suma_punktow(gracz) < 21:
        # Krupier dobiera karty az ich wartosc bedzie >= 17
        krupier.append(losowanie_kart(talia_kart))

    # Drukowanie widocznych kart krupiera i gracza oraz sprawdzanie wyniku gry
    drukowanie_kart(grafika_kart(krupier, karta_odkryta=True), grafika_kart(gracz, karta_odkryta=True))
    print(porownanie_wynikow(suma_punktow(gracz), suma_punktow(krupier)))


while input("Czy chcesz zagrac w Blackjack? (y/n) ").lower() == "y":
    blackjack()
