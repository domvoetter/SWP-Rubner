from DoppeltVerketteteListe import *
import random

def create():
    list = DoppeltVerketteteListe()
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    #list.writeList()
    return list


def start(list, list2):
    do = input("Was wollen Sie tun? \n 1: append \
        \n 2: insert \n 3: remove \
        \n 4: index \n 5: Ausgeben \n 6: count \
        \n 7: clear \n 8: copy \
        \n 9: extend \n 10: pop \
        \n 11: sort      ")
    if do == "1": 
        list.writeList()
        x = input("Was wollen Sie drann hängen?   ")
        list.addLast(x)
        list.writeList()
        start(list, list2)
    if do == "2": 
        list.writeList()
        x = input("Was wollen Sie einfügen   ")
        y = input("Nach was soll es eingefügt werden?   ")
        list.insertAfter(int(y), int(x))
        list.writeList()
        start(list, list2)
    if do == "3": 
        list.writeList()
        x = input("Was wollen Sie löschen?   ")
        a = list.delete(int(x))
        list.writeList()
        start(list, list2)
    if do == "4": 
        list.writeList()
        x = input("Von was wollen Sie den index haben?   ")
        print("Index: " + str(list.index(int(x))))
        start(list, list2)
    if do == "5": 
        list.writeList()
        start(list, list2)
    if do == "6":
        list.writeList()
        print("Länge: " + str(list.printLength()))
        start(list, list2)
    if do == "7":
        list.clear()
        list.writeList()
        start(list, list2)
    if do == "8":
        print("Kopierte Liste: \n")
        copied = list.copyList()
        copied.writeList()
        start(list, list2)
    if do == "9":
        print("Liste 1: \n")
        list.writeList()
        print("\n Liste 2: \n")
        list2.writeList()
        print("\n neue Liste 1: \n")
        list.extend(list2)
        list.writeList()
        start(list, list2)
    if do == "10":
        list.writeList()
        x = input("An welcher Stelle steht das Element, das sie löschen wollen?   ")
        a = list.pop(int(x))
        list.writeList()
        start(list, list2)
    if do == "11":
        print("\n Vorher: \n")
        list.writeList()
        print("\n Nachher: \n")
        list.sort()
        #list.writeList()
        start(list, list2)
    if do == "exit":
        return
    else:
        print("ungültige Eingabe")
        start(list, list2)


if __name__ == "__main__":
    list = create()
    list2 = DoppeltVerketteteListe()
    list2.addLast(random.randint(0,100))
    start(list, list2)