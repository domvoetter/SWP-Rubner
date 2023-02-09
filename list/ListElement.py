class ListElement:

    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None

    
    def setNextElem(self, elem):
        self.nextElem = elem

    def getNextElem(self):
        return self.nextElem

    def getObj(self):
        return self.obj

    def setObj(self, obj):
        self.obj = obj