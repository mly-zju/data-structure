from stack import Stack


def checkBalance(expression):
    s = Stack()
    l = len(expression)
    index = 0
    while index < l:
        symbol = expression[index]
        if symbol in '([{':
            s.push(symbol)
        elif symbol in ')]}':
            if s.isEmpty():
                return False
            begin = '([{'
            end = ')]}'
            match = begin.index(s.pop()) == end.index(symbol)
            if not match:
                return False
        index = index + 1
    if s.isEmpty():
        return True
    else:
        return False


print(checkBalance('[(2+3)*5+{2/3}]'))
