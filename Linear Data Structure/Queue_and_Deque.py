# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:44:53 2021

@author: Shawn
"""

# Implement Queue with Python
# The first item is the rear of the queue
class Queue:
    # initialize with a list[]
    def __init__(self):
        self.items = []
    
    # decide if it is empty
    def isEmpty(self):
        return self.items == []
    
    # add an item with enqueue(item)
    def enqueue(self, item):
        self.items.insert(0, item)
    
    # get an item from the head of the queue with dequeue()
    def dequeue(self):
        return self.items.pop()
    
    # get the length of the Queue
    def size(self):
        return len(self.items)
    
    # show the queue
    def show(self):
        print(self.items)

# Implement Dequeue with Python
# The first item is the rear of the dequeue
# The last item is the head of the dequeue
class Deque:
    # initialize with a list[]
    def __init__(self):
        self.items = []
    
    # decide if it is empty
    def isEmpty(self):
        return self.items == []
    
    # add an item with addFront(item)
    def addFront(self, item):
        self.items.append(item)
    
    # add an item with addRear(item)
    def addRear(self, item):
        self.items.insert(0, item)
    
    # get an item from the head of the queue with removeFront()
    def removeFront(self):
        return self.items.pop()
    
    # get an item from the head of the queue with removeRear()
    def removeRear(self):
        return self.items.pop(0)
    
    # get the length of the Queue
    def size(self):
        return len(self.items)
    
    # show the queue
    def show(self):
        print(self.items)


# Solve Josephus Problem With Queue
def Josephus(totalNum, k):
    q = Queue()
    # tag each person and enqueue them into a queue
    for i in range(totalNum):
        q.enqueue(int(i+1))
    q.show()
    
    num = 0
    while q.size() != 1:
        for i in range(k-1):
            q.enqueue(q.dequeue())
        out = q.dequeue()
        num += 1
        print('{0:<3} OUT: {1:<3} REST: {2:<12}'.format(num, out, q.size()))
    print('WIN: {0}'.format(q.dequeue()))

# Implement Palindrome Checker With Deque
def palChecker(aString):
    Deq = Deque()
    for ch in aString:
        Deq.addFront(ch)
    check = True
    while Deq.size() > 1 and check:
        front = Deq.removeFront()
        rear = Deq.removeRear()
        if front != rear:
            check = False
    print(check)
    return check

if __name__ == '__main__':
    #Josephus(20, 4)
    #palChecker('asdfghjklkjhgfdsa')
    pass

















