# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:35:57 2021

@author: Shawn
"""

# Set The Node Class
class Node():
    # initialize
    def __init__(self, initData):
        self.data = initData
        self.next = None
    
    # get the data of the Node
    def getData(self):
        return self.data
    
    # get the next Node
    def getNext(self):
        return self.next
    
    # set data
    def setData(self, newData):
        self.data = newData
    
    # set the next Node
    def setNext(self, newNext):
        self.next = newNext
    
    # show the Node
    def show(self):
        return str(self.data)

# Create The Unordered List Class
class UnorderedList():
    # initialize
    def __init__(self):
        self.head = None

    # decide if it is empty
    def isEmpty(self):
        return self.head == None
    
    # complete Add function
    def add(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode
    
    # count the length of the unordered list
    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    # search the item
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    # add an item at the end of list
    def append(self, item):
        current = self.head
        previous = Node(None)
        while current != None:
            previous = current
            current = current.getNext()
        newNode = Node(item)
        previous.setNext(newNode)
        pass
    
    # insert an item at specific position
    def insert(self, pos, item):
        count = 0
        previous = None
        current = self.head
        if pos > self.length():
            print('Position out of range')
        else:
            while count < pos:
                previous = current
                current = current.getNext()
                count += 1
            newNode = Node(item)
            newNode.setNext(current)
            previous.setNext(newNode)
    
    # return the index of an item
    def index(self, item):
        current = self.head
        count = 0
        while current != None:
            if current.getData() == item:
                return count
            else:
                current = current.getNext()
                count += 1
        return None

    # return the first item
    def pop(self):
        return self.head.getData()
    
    # remove the item
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    # show the Unordered list
    def show(self):
        current = self.head
        i = 1
        while i < self.length():
            print(current.show() + '-->', end = '')
            current = current.getNext()
            i += 1
        print(current.show())
            
# Create The ordered List Class
class OrderedList():
    # initialize
    def __init__(self):
        self.head = None
        
     # decide if it is empty
    def isEmpty(self):
        return self.head == None
    
    # count the length of the ordered list
    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    # search the item
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        print(found)
        return found
    
    # complete Add function
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        newNode = Node(item)
        if previous == None:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            newNode.setNext(current)
            previous.setNext(newNode)
            
    # show the Ordered list
    def show(self):
        current = self.head
        i = 1
        while i < self.length():
            print(current.show() + '-->', end = '')
            current = current.getNext()
            i += 1
        print(current.show())

if __name__ == '__main__':
    pass
        
























