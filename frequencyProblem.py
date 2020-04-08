#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 

# Complete the freqQuery function below.
def freqQuery(queries):
    valueDict = defaultdict(int)
    freqDict = defaultdict(int)
    ans = []
    for [i,x] in queries:
        if i==1:
            freqDict[valueDict[x]] = max(0,freqDict[valueDict[x]] -1)
            valueDict[x] += 1
            freqDict[valueDict[x]] += 1
        elif i==2:
            freqDict[valueDict[x]] = max(0,freqDict[valueDict[x]] -1)
            valueDict[x] = max(0,valueDict[x]-1)
            freqDict[valueDict[x]] += 1
        elif i==3:
            ans.append(1 if freqDict[x]>0 else 0)
        #print(valueDict,freqDict)
    return ans

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
