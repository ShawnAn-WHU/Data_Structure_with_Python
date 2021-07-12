# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:45:06 2021

@author: Shawn
"""

# O(n^2)
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


# O(n^2)
def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range (passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1

# O(n^2)
def selectionSort(alist):
    for num in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for i in range(1, num + 1):
            if alist[i] > alist[positionOfMax]:
                positionOfMax = i
    alist[num], alist[positionOfMax] = alist[positionOfMax], alist[num]

# 0(nlogn)
def mergeSort(alist):
    print('Spliting ', alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthand = alist[ : mid]
        righthand = alist[mid : ]
        
        mergeSort(lefthand)
        mergeSort(righthand)
        
        i = 0
        j = 0
        k = 0
        while i < len(lefthand) and j < len(righthand):
            if lefthand[i] < righthand[j]:
                alist[k] = lefthand[i]
                i += 1
            else:
                alist[k] = righthand[j]
                j += 1
            k += 1
        while i < len(lefthand):
            alist[k] = lefthand[i]
            i += 1
            k += 1
        while j < len(righthand):
            alist[k] = righthand[j]
            j += 1
            k += 1
    print('Merging ', alist)
    return alist

# O(nlogn)
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)
    return alist

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotvalue = alist[0]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -=1
        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark





























