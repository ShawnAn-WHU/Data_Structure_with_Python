# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:41:50 2021

@author: Shawn
"""

# Implement Stack With Python
class Stack:
    # initialize with a list[]
    def __init__(self):
        self.items = []
        
    # decide if it is empty
    def isEmpty(self):
        return self.items == []
    
    # Add an item with push(item)
    def push(self, item):
        self.items.append(item)
        
    # get an item from the top and delete the item with pop()
    def pop(self):
        return self.items.pop()
    
    # get an item fron the top but not delete the item from Stack with peek()
    def peek(self):
        return self.items[len(self.items)-1]
    
    # get the length of the Stack
    def size(self):
        return len(self.items)
    
    # show the queue
    def show(self):
        print(self.items)

# Match Brackets only for '()'
def matchBrackets(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        # if '(', push into Stack
        if symbolString[index] == '(':
            s.push(symbolString[index])
        # else, see if Stack is empty. Empty:False; Not Empty:pop to delete '('
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False

# Match Brackets for '()', '[]', '{}'
def matchBracketsUpdate(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        if symbolString[index] in '([{':
            s.push(symbolString)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                # decide if the two brackets are a pair
                if not match(top, symbolString[index]):
                    balanced = False
        index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False

# a function for matchBracketsUpdate
def match(openBracket, closeBracket):
        openBrackets = '([{'
        closeBrackets = ')]}'
        return openBrackets.index(openBracket) == closeBrackets.index(closeBracket)

# Convert Decimal Number to Any Base Number
def baseConvert(decNum, base):
    digits = '0123456789abcdef'
    s = Stack()
    while decNum > 0:
        rem = decNum % base
        s.push(rem)
        decNum = decNum // base
    newString = ''
    while not s.isEmpty():
        newString = newString + digits[s.pop()]
    return newString

# Convert Middle Order Expression to Post Order Expression
def middleOdertoPostOder(middleOrder):
    import string
    # set the priority of the operation symbol
    dict = {}
    dict['*'] = 3
    dict['/'] = 3
    dict['+'] = 2
    dict['-'] = 2
    dict['('] = 1
    
    s = Stack()
    postOrder = []
    tokenList = middleOrder.split()
    for token in tokenList:
        if token in string.ascii_uppercase:
            postOrder.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            top = s.pop()
            while top != '(':
                postOrder.append(top)
                top = s.pop()
        else:
            # decide the priority of the operation symbol
            while (not s.isEmpty()) and (dict[s.peek()] > dict[token]):
                postOrder.append(s.pop())
            s.push(token)
    while not s.isEmpty():
        postOrder.append(s.pop())
    
    return " ".join(postOrder)

# Compute The Post Order Expression
def OpPostOrder(postOrder):
    s = Stack()
    tokenList = postOrder.split(' ')
    for token in tokenList:
        if token in '0123456789':
            s.push(int(token))
        else:
            operand2 = s.pop()
            operand1 = s.pop()
            result = doMath(token, operand1, operand2)
            s.push(result)
    return s.pop()

# A Function For OpPostOrder(postOrder)
def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

if __name__ == '__main__':
    pass
















