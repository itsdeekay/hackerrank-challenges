#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n,m, queries):
    newArray = [0]*(n+2)
    for i in queries:
        newArray[i[0]] += i[2]
        newArray[i[1]+1] -= i[2] 
    maxx = 0
    x = 0
    for i in range(1,n+1):
        x += newArray[i]
        if(x>maxx):
            maxx = x
    return maxx
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n,m, queries)

    print(str(result))

