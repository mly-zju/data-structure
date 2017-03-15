class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


if __name__ == '__main__':

    s = Stack()
    sentence = raw_input('please enter a sentence\n')
    l = len(sentence)
    i = 0
    while i < l:
        s.push(sentence[i])
        i += 1

    reverse = ''
    while s.size() > 0:
        reverse = reverse + s.pop()

    print(reverse)
