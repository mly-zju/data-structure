from stack import Stack


def decimalTrans(number, base):
    s = Stack()
    digits = "0123456789ABCDEF"
    while number > 0:
        s.push(number % base)
        number = number // base
    newNum = ''
    while not s.isEmpty():
        newNum = newNum + digits[s.pop()]
    return newNum


print(decimalTrans(256, 16))
