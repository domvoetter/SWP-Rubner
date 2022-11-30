class Person:
    def __init__(self, vorname, nachname, geburtsdatum, geschlecht):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.geschlecht = geschlecht

        def __str__(self):
            return f"{self.vaorname} {self.nachname} geboren am {self.geburtsdatum} ({self.geschlecht})"