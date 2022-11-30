from SWP-Runner.OOP_uebung.Person import Person


class Mitarbeiter(Person):
    def __init__(self, vorname, nachname, geburtsdatum, geschlecht, personalnummer):
        super().__init__(vorname, nachname, geburtsdatum, geschlecht)
        self.personalnummer = personalnummer