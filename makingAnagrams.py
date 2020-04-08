#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    aDict =  defaultdict(int)
    delete =  0
    for i in a:
        aDict[i] +=1
    for i in b:
        aDict[i] -= 1
    for i in aDict:
        delete += abs(aDict[i])
    return delete
    
if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)
