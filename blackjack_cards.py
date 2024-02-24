def pobierz_grafike(nazwa_karty, znak_koloru, widzialnosc_kart):
    """
    Funkcja przechowywujaca grafiki kart, ktora na podstawie otrzymanych
    parametrow zwraca karty odkryte/zakryte (widzialnosc_kart) oraz w
    przypadku odkrytych z nazwa karty i jej znakiem koloru odpowiadajacym
    danej karcie.
    """
    if widzialnosc_kart:
        if nazwa_karty != "10":
            karta = [
                "╔══════╗",
                f"║ {nazwa_karty}    ║",
                "║      ║",
                f"║    {znak_koloru} ║",
                "╚══════╝",
            ]
        else:
            karta = [
                "╔══════╗",
                f"║ {nazwa_karty}   ║",
                "║      ║",
                f"║    {znak_koloru} ║",
                "╚══════╝",
            ]
    if not widzialnosc_kart:
        karta = [
            "╔══════╗",
            "║░░░░░░║",
            "║░░░░░░║",
            "║░░░░░░║",
            "╚══════╝",
        ]

    return karta
