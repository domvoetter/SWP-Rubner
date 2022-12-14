from Person import Person

class Mitarbeiter(Person):
    def __init__(self, person, personalnummer):
        super().__init__(person.vorname, person.nachname, \
            person.geburtsdatum, person.geschlecht)
        self.personalnummer = personalnummer

    def __str__(self):
        return f"{super().__str__()} Nummer: {self.personalnummer} \n"