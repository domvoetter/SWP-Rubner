from copy import deepcopy

class arrayList:
    def init(self):
        self.items = []

    def append(self, o):
        self.items.append(o)
        
    def clear(self):
        self.items.clear()

    def copy(self):
        newlist = arrayList()
        newlist.items = deepcopy(self.items)
        return newlist

    def count(self):
        return len(self.items)

    def extend(self, o):
        self.items.extend(o)

    def index(self, o):
        return self.items.index(o)

    def insert(self, index, o):
        self.items.insert(index, o)

    def pop(self, o):
        self.items.pop(o)

    def remove(self, o):
        self.items.remove(o)

    def sort(self):
        self.items.sort()

    def getFirstElem(self):
        self.items[0]

    def getLastElem(self):
        self.items[self.length -1] 

    def writeList(self):
        for i in self.items:
            print(i)

    def reverse(self):
        self.items.reverse()