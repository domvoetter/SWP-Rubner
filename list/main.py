import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from EinfachVerketteteListe import *
import random
from EinfachVerketteteListe import *
from ListElementDoppelt import *
from DoppeltVerketteteListe import *

def createEinfach():
    list = EinfachVerketteteListe()
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    #list.writeList()
    return list

def createDoppelt():
    list = DoppeltVerketteteListe()
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    list.addLast(random.randint(0, 1000))
    return list


def start(list, list2, list3):
    option = input("Mit was wollen Sie arbeiten? Einfach, Doppelt, Tabelle? \n")
    if option == "Einfach":
        do = input("Was wollen Sie tun? \n 1: append \
            \n 2: insert \n 3: remove \
            \n 4: index \n 5: Ausgeben \n 6: count \
            \n 7: clear \n 8: copy \
            \n 9: extend \n 10: pop \
            \n 11: sort  \n 12: reverse   \n")
        if do == "1": 
            list.writeList()
            x = input("Was wollen Sie drann hängen?   ")
            list.addLast(int(x))
            list.writeList()
            start(list, list2, list3)
        if do == "2": 
            list.writeList()
            x = input("Was wollen Sie einfügen   ")
            y = input("Nach was soll es eingefügt werden?   ")
            list.insertAfter(int(y), int(x))
            list.writeList()
            start(list, list2, list3)
        if do == "3": 
            list.writeList()
            x = input("Was wollen Sie löschen?   ")
            a = list.delete(int(x))
            list.writeList()
            start(list, list2, list3)
        if do == "4": 
            list.writeList()
            x = input("Von was wollen Sie den index haben?   ")
            print("Index: " + str(list.index(int(x))))
            start(list, list2, list3)
        if do == "5": 
            list.writeList()
            start(list, list2, list3)
        if do == "6":
            list.writeList()
            print("Länge: " + str(list.printLength()))
            start(list, list2, list3)
        if do == "7":
            list.clear()
            list.writeList()
            start(list, list2, list3)
        if do == "8":
            list.writeList()
            print("Kopierte Liste: \n")
            copied = list.copyList()
            copied.writeList()
            start(list, list2, list3)
        if do == "9":
            print("Liste 1: \n")
            list.writeList()
            print("\n Liste 2: \n")
            list2.writeList()
            print("\n neue Liste 1: \n")
            list.extend(list2)
            list.writeList()
            start(list, list2, list3)
        if do == "10":
            list.writeList()
            x = input("An welcher Stelle steht das Element, das sie löschen wollen?   ")
            a = list.pop(int(x))
            list.writeList()
            start(list, list2, list3)
        if do == "11":
            print("\n Vorher: \n")
            list.writeList()
            print("\n Nachher: \n")
            list.sort()
            list.writeList()
            start(list, list2, list3)
        if do == "12":
            list.writeList()
            list.reverse()
            print("\n Nach dem umdrehen: n")
            list.writeList()
        if do == "exit":
            exit
        else:
            print("ungültige Eingabe")
            start(list, list2, list3)
    if option == "Doppelt":
        do = input("Was wollen Sie tun? \n 1: append \
            \n 2: insert \n 3: remove \
            \n 4: index \n 5: Ausgeben \n 6: count \
            \n 7: clear \n 8: copy \
            \n 9: extend \n 10: pop \
            \n 11: sort  \n 12: reverse  \n")
        if do == "1": 
            list3.writeList()
            x = input("Was wollen Sie drann hängen?   ")
            list3.addLast(int(x))
            list3.writeList()
            start(list, list2, list3)
        if do == "2": 
            list3.writeList()
            x = input("Was wollen Sie einfügen   ")
            y = input("Nach was soll es eingefügt werden?   ")
            list3.insertAfter(int(y), int(x))
            list3.writeList()
            start(list, list2, list3)
        if do == "3": 
            list3.writeList()
            x = input("Was wollen Sie löschen?   ")
            a = list3.delete(int(x))
            list3.writeList()
            start(list, list2, list3)
        if do == "4": 
            list3.writeList()
            x = input("Von was wollen Sie den index haben?   ")
            print("Index: " + str(list3.index(int(x))))
            start(list, list2, list3)
        if do == "5": 
            list3.writeList()
            start(list, list2, list3)
        if do == "6":
            list3.writeList()
            print("Länge: " + str(list3.printLength()))
            start(list, list2, list3)
        if do == "7":
            list3.clear()
            list3.writeList()
            start(list, list2, list3)
        if do == "8":
            list3.writeList()
            print("Kopierte Liste: \n")
            copied = list3.copyList()
            copied.writeList()
            start(list, list2, list3)
        if do == "9":
            list4 = DoppeltVerketteteListe()
            list4.addLast(6)
            list4.addLast(7)
            list4.addLast(8)
            print("Liste 1: \n")
            list3.writeList()
            print("\n Liste 2: \n")
            list4.writeList()
            print("\n neue Liste 1: \n")
            list3.extend(list4)
            list3.writeList()
            start(list, list2, list3)
        if do == "10":
            list3.writeList()
            x = input("An welcher Stelle steht das Element, das sie löschen wollen?   ")
            a = list3.pop(int(x))
            list3.writeList()
            start(list, list2, list3)
        if do == "11":
            print("\n Vorher: \n")
            list3.writeList()
            print("\n Nachher: \n")
            list3.sort()#
            list3.writeList()
            start(list, list2, list3)
        if do == "12":
            list3.writeList()
            list3.reverse()
            print("\n Nach dem umdrehen: n")
            list3.writeList()
        if do == "exit":
            exit
        else:
            print("ungültige Eingabe")
            start(list, list2, list3)
    if option == "Tabelle":
        np.random.seed(0)
        fig, ax = plt.subplots()

        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')

        df = pd.read_excel("list/Aufwandsklassen.xlsx")

        table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

        fig.tight_layout()
        plt.show()
    if option == "exit":
        exit
    else:
        print("Ungültige Eingabe")
        start(list, list2, list3)


if __name__ == "__main__":
    list = createEinfach()
    list2 = EinfachVerketteteListe()
    list3 = createDoppelt()
    list2.addLast(random.randint(0,100))
    start(list, list2, list3)