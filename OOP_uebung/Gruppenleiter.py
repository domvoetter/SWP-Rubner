from Mitarbeiter import *
from Person import *

class Gruppenleiter(Mitarbeiter):
    def __init__(self, mitarbeiter, gruppenname):
        super().__init__(Person(mitarbeiter.vorname, \
            mitarbeiter.nachname, mitarbeiter.geburtsdatum, \
                mitarbeiter.geschlecht), mitarbeiter.personalnummer)
        self.gruppenname = gruppenname

    def __str__(self):
        return f"{super().__str__()} Gruppenname: {self.gruppenname}"