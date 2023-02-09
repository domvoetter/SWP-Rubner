from Firma import *
from Abteilung import *
from Gruppenleiter import *
from Mitarbeiter import *
from Person import *

def create():
    f =  Firma("Firma 1")
    a = Abteilung("Abteilung1")
    a2 = Abteilung("Abteilung2")
    p = Person("Dominik", "Vötter", "26-06-2004", "m")
    p2 = Person("Lisa", "Musterfrau", "02-02-2005", "w")
    m = Mitarbeiter(p, 1)
    m2 = Mitarbeiter(p, 2)
    m3 = Mitarbeiter(p2, 3)
    g = Gruppenleiter(m, "TeamCool")

    a.mitarbeiter.append(m)
    a.mitarbeiter.append(m3)
    a2.mitarbeiter.append(m)
    a2.mitarbeiter.append(m2)
    f.abteilungen.append(a)
    f.abteilungen.append(a2)
    a.gruppenleiter.append(g)

    return f

def addMitarbeiter(firma):
    abteilung = input("Abteilung: ")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    geburtsdatum = input("Geburtsdatum (yyyy-mm-dd): ")
    geschlecht = input("Geschlecht: ")
    nummer = input("Nummer: ")

    p = Person(vorname, nachname, geburtsdatum, geschlecht)

    for a in firma.abteilungen:
        if a.abteilungsname == abteilung:
            a.mitarbeiter.append(Mitarbeiter(p, nummer))

    start(firma)


def alleMitarbeiter(firma):
    abteilung = input("Welche Abteilung? ")
    for a in firma.abteilungen:
        if a.abteilungsname == abteilung:
            for m in a.mitarbeiter:
                print(m)
    start(firma)


def start(firma):
    do = input("Was wollen Sie sehen? \n 1: Mitarbeiteranzahl \
        \n 2: Gruppenleiteranzahl \n 3: Abteilungsanzahl \
        \n 4: Groesste Abteilung \n 5: Verhältniss f/m \n 6: Mitarbeiter hinzufuegen \
        \n 7: Alle Mitarbeiter anzeigen \n")
    if do == "1": 
        firma.anzMitarbeiter()
        start(firma)
    if do == "2": 
        firma.anzGruppenleiter()
        start(firma)
    if do == "3": 
        firma.anzAbteilungen()
        start(firma)
    if do == "4": 
        firma.groessteAbteilung()
        start(firma)
    if do == "5": 
        firma.frauenmaenner()
        start(firma)
    if do == "6":
        addMitarbeiter(firma)
    if do == "7":
        alleMitarbeiter(firma)
    if do == "exit":
        return
    else:
        print("ungültige Eingabe")
        start(firma)


if __name__ == "__main__":
    firma = create()
    start(firma)