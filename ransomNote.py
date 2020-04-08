#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mDict = {}
    
    for k in magazine:
        if k in mDict:
            mDict[k] += 1
        else:
            mDict[k] = 1
    for k in note:
        if k in mDict and mDict[k]>0:
                mDict[k] -= 1
        else:
            return 'No'
    return 'Yes'
    
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    result = checkMagazine(magazine, note)

    print(result)
