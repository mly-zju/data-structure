class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.insert(0, element)

    def dequeue(self):
        value = self.items.pop()
        return value

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0


if __name__ == '__main__':
    q = Queue()
    q.enqueue('first')
    q.enqueue('second')
    print(q.size())
    print(q.dequeue())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.isEmpty())
