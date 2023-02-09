from enum import Enum

class Geschlecht(Enum):
    m = 1
    w = 2

class Person:
    def __init__(self, vorname, nachname, geburtsdatum, geschlecht):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.geschlecht = geschlecht

    def __str__(self):
        return f"Name: {self.vorname} {self.nachname} \
            Geburtsdatum: {self.geburtsdatum} \
                Geschlecht: {self.geschlecht} \n"