#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def merge(arr,l,r):
    i,j,k = 0,0,0
    lLen = len(l)
    rLen = len(r)
    inversions = 0
    while(i<lLen and j <rLen):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i+= 1
        else:
            arr[k] = r[j]
            j += 1
            inversions += lLen - i
        k += 1

    while(i<lLen):
        arr[k] = l[i]
        i,k= i+1, k+1

    while(j<rLen):
        arr[k] = r[j]
        j,k= j+1, k+1
        
    return inversions

def mergeSort(arr):
    l = len(arr)
    if(l>2):
        mid = l//2
        lh,rh = arr[:mid],arr[mid:]
        return mergeSort(lh) + mergeSort(rh) + merge(arr,lh,rh)
    elif(l==2 and arr[0]>arr[1]):
        arr[0],arr[1] = arr[1],arr[0]
        return 1
    return 0

def countInversions(arr):
    return mergeSort(arr)
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(result)
