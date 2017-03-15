class Dequeue:
    def __init__(self):
        self.items = []

    def addFront(self, element):
        self.items.append(element)

    def removeFront(self):
        return self.items.pop()

    def addRear(self, element):
        self.items.insert(0, element)

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0
