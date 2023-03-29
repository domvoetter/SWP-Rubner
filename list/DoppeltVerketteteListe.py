from copy import copy
from ListElementDoppelt import *

class DoppeltVerketteteListe:

    def __init__(self):
        self.startElem = ListElementDoppelt(None)
        self.lastElem = ListElementDoppelt(None)
        self.startElem.setNextElem(self.lastElem)
        self.lastElem.setPrevElem(self.startElem)


    # append
    def addLast(self, o):
        if self.startElem.getObj() == None:
            self.startElem = ListElementDoppelt(o)
            self.lastElem = self.startElem
        else:
            newElem = ListElementDoppelt(o)
            lastElement = self.lastElem
            lastElement.setNextElem(newElem)
            newElem.setPrevElem(lastElement)
            self.lastElem = newElem


    # insert
    def insertAfter(self, prevItem, newItem):
        insertAfterElem = ListElementDoppelt(prevItem)
        newItem2 = ListElementDoppelt(newItem)
        if insertAfterElem.obj == self.startElem.obj:
            nextElem = self.startElem.getNextElem()
            self.startElem.setNextElem(newItem2)
            newItem2.setNextElem(nextElem)
            newItem2.setPrevElem(self.startElem)
        else:
            nextElem = ListElementDoppelt(None)
            pointerElem = self.startElem.getNextElem()
            while pointerElem != None and pointerElem.getObj() != prevItem:
                pointerElem = pointerElem.getNextElem()
            newElem = ListElementDoppelt(newItem)
            if pointerElem != None:
                nextElem = pointerElem.getNextElem()
                pointerElem.setNextElem(newElem)
                newElem.setNextElem(nextElem)
                newElem.setPrevElem(pointerElem)
            if nextElem != None:
                nextElem.setPrevElem(newElem)


    def insertBefore(self, insertElem, newItem):
        newElem = ListElementDoppelt(newItem)
        pointerElem = self.startElem.getNextElem()
        while pointerElem != None:
            if pointerElem.getObj() == insertElem:
                newElem.setPrevElem(pointerElem.getPrevElem())
                pointerElem.getPrevElem().setNextElem(newElem)
                pointerElem.setPrevElem(newElem)
                newElem.setNextElem(pointerElem)
                break
            pointerElem = pointerElem.getNextElem()


    # remove
    def delete(self, o):
        le = self.startElem
        while le.getNextElem() != None and le.getObj() != o:
            if le.getNextElem().getObj() == o:
                if le.getNextElem().getNextElem() != None:
                    le.setNextElem(le.getNextElem().getNextElem())
                    le.getNextElem().setPrevElem(le)
                else:
                    le.setNextElem(None)
                    break
            le = le.getNextElem()
        return o


    # index
    def index(self, o):
        le = self.startElem
        cnt = 0
        while le != None:
            cnt += 1
            if le.getObj() == o:
                return cnt-1
            le = le.nextElem
        return None


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
            print(str(le.getObj()) + "  ")
            le = le.getNextElem()


    # count
    def printLength(self):
        le = self.startElem
        cnt = 0
        while le != None:
            cnt += 1
            le = le.nextElem
        return cnt
    

    # clear (ganze Liste löschen)
    def clear(self):
        self.startElem.setNextElem(None)
        self.endElem = None
        self.startElem = None

    
    # copy
    def copyList(self):
        new_list = DoppeltVerketteteListe()
        current_elem = self.startElem
        while current_elem.getNextElem() is not None:
            new_list.addLast(current_elem.getNextElem().getObj())
            current_elem = current_elem.getNextElem()
        return new_list


    # extend (hinzufügen aller Elemente einer anderen Liste)
    def extend(self, secondList):
        le = secondList.startElem.getNextElem()
        while le is not None:
            self.addLast(le.getObj())
            le = le.getNextElem()


    # pop ( löscht den Eintrag aus der Liste des übergebenen Index und liefert dessen Inhalt als Rückgabewert )
    def pop(self, index):
        le = self.startElem
        for c in range(index):
            le = le.getNextElem()
        self.delete(le.getObj())
        return le.getObj()


    # sort
    def sort(self):
        if not self.startElem:
            return
    
        swapped = True
        while swapped:
            swapped = False
            current = self.startElem
            while current.nextElem:
                runner = current.nextElem
                if current.obj is not None and runner.obj is not None: # Vergleichsbedingung hinzufügen
                    if current.obj > runner.obj:
                        current.obj, runner.obj = runner.obj, current.obj
                        swapped = True
                current = current.nextElem


    def reverse(self):
        currentElem = self.startElem
        while currentElem:
            nextElem = currentElem.getNextElem()
            currentElem.nextElem = currentElem.getPrevElem()
            currentElem.prevElem = nextElem
            if not nextElem:
                self.startElem = currentElem
            currentElem = nextElem