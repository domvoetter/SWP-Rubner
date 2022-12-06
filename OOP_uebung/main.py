from Firma import *
from Abteilung import *
from Gruppenleiter import *
from Mitarbeiter import *
from Person import *

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

#f.anzMitarbeiter()
#f.anzGruppenleiter()
#f.anzAbteilungen()
#f.groessteAbteilung()
f.frauenmaenner()

#print(str(p))