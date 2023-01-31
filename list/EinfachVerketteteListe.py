from ListElement import *

class EinfachVerketteteListe:

    def __init__(self):
        self.startElem = ListElement("Kopf")


    # append
    def addLast(self, o):
        newElem = ListElement(o)
        lastElem = self.getLastElem()
        lastElem.setNextElem(newElem)


    # insert
    def insertAfter(self, prevItem, newItem):
        pointerElem = self.startElem.getNextElem()
        while pointerElem != None and pointerElem.getObj() != prevItem:
            pointerElem = pointerElem.getNextElem()
        newElem = ListElement(newItem)
        nextElem = pointerElem.getNextElem()
        pointerElem.setNextElem(newElem)
        newElem.setNextElem(nextElem)


    # remove
    # TODO: Inhalt des gelöschten Elements als Rückgabewert
    def delete(self, o):
        le = self.startElem
        while le.getNextElem() != None and le.getObj() != o:
            if le.getNextElem().getObj() == o:
                if le.getNextElem().getNextElem() != None:
                    le.setNextElem(le.getNextElem().getNextElem())
                else:
                    le.setNextElem(None)
                    break
            le = le.getNextElem()

    # index
    # TODO: index zurückgeben
    def find(self, o):
        le = self.startElem
        while le != None:
            if le.getObj() == o:
                return True
            le = le.nextElem
        return False

    
    def getFirstElem(self):
        return self.startElem

    
    def getLastElem(self):
        le = self.startElem
        while le.getNextElem() != None:
            le = le.getNextElem()
        return le

    def writeList(self):
        le = self.startElem
        while le != None:
            print(str(le.getObj()) + "\n")
            le = le.getNextElem()

    
    # count
    def printLength(self):
        le = self.startElem
        cnt = 0
        while le != None:
            cnt += 1
            le = le.nextElem
        return cnt

    def index(self, o):
        le = self.startElem
        cnt = 0
        while le != None:
            cnt += 1
            if le.nextElem.getObj() == o:
                return cnt
            le = le.nextElem
        return None

    # clear (ganze Liste löschen)
    # copy
    # extend (hinzufügen aller Elemente einer anderen Liste)
    # pop ( löscht den Eintrag aus der Liste des übergebenen Index und liefert dessen Inhalt als Rückgabewert )
    # sort