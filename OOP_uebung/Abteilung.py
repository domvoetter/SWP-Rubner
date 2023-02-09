class Abteilung:
    def __init__(self, abteilungsname):
        self.abteilungsname = abteilungsname
        self.mitarbeiter = []
        self.gruppenleiter = []

    def __str__(self):
        return f"Name: {self.abteilungsname} \
             Anzahl der Mitarbeiter: {len(self.mitarbeiter)} \
                 Anzahl der Gruppenleiter: {len(self.gruppenleiter)}"
