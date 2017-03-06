#!/usr/bin/env python3

import random

def tipp():
    tipp = []
    schein = list(range(1, 49))
    for i in range(6):
        valid = False
        while not valid:
            print("Zahl eingeben: ")
            zahl = input()
            # versuche die eingebene zahl vom tippschein zu entfernen.
            # klappt das füge sie dem tipp hinzu und setze valid auf true
            # dadurch wird die nächste zahl abgefragt
            # tritt ein fehler auf (except) dann versuche es nochmal
            try:
                schein.remove(int(zahl))
                tipp.append(int(zahl))
                valid = True
            except ValueError:
                print("Zahl ist nicht auf dem Schein")
                pass
    return tipp

def ziehen():
    ziehung = []
    kugeln = list(range(1, 49))
    # bestimme einen zufälligen index der liste kugeln von 0 bis zur länge der liste -1
    # eine liste mit 10 elementen hat den index 0...9 deswegen -1
    # entferne die kugel aus den kugeln -> keine doppelziehungen
    for i in range(6):
        kugel_nr = random.randint(0, len(kugeln) - 1)
        ziehung.append(kugeln[kugel_nr])
        kugeln.remove(kugeln[kugel_nr])

    return ziehung



tipp = tipp()
ziehung = ziehen()
