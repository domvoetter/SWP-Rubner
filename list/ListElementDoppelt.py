class ListElementDoppelt:

    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None
        self.prevElem = None

    
    def setNextElem(self, elem):
        self.nextElem = elem

    def getNextElem(self):
        return self.nextElem
    
    def setPrevElem(self, elem):
        self.prevElem = elem

    def getPrevElem(self):
        return self.prevElem

    def getObj(self):
        return self.obj

    def setObj(self, obj):
        self.obj = obj