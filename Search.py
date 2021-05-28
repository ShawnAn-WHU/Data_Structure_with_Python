# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:37:42 2021

@author: Shawn
"""

# Sequential Search: O(n)
def SequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

# Sequential Search for Ordered List: O(n)
def OrderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

# Binary Search: O(logn)
def BinarySearch(alist, item):
    found = False
    first = 0
    last = len(alist) - 1
    while first < last and not found:
        mid = (first + last) // 2
        if alist[mid] < item:
            first = mid + 1
        elif alist[mid] > item:
            last = mid - 1
        else:
            found = True
    return found

# Set Hash for String
def HashforString(string, tableSize):
    sum = 0
    for s in string:
        sum += ord(s)
    return sum % tableSize

# Create HashTable Class
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * 11
        self.data = [None] * 11
        
    def hashfunction(self, key, size):
        return key % size
    
    def rehash(self, oldHash, size):
        return(oldHash + 1) % size
    
    def put(self, key, data):
        hashValue = self.hashfunction(key, len(self.slots))
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                data[hashValue] = data
            else:
                nextslot = self.rehash(hashValue, len(self.slots))
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
                          nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[hashValue] = key
                    self.data[hashValue] = data
                else:
                    self.data[nextslot] = data
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        pos = startslot
        while self.slots[pos] != None and \
              not stop and not found:
                  if self.slots[pos] == key:
                      found = True
                      data = self.data[pos]
                  else:
                      pos = self.rehash(pos, len(self.slots))
                      if pos == startslot:
                          stop = True
        return data

def __getitem__(self, key):
    return self.get(key)

def __setitem__(self, key, data):
    self.put(key, data)
























