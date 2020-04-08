#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    arrayLen = len(a)
    b = [0]*arrayLen

    for i in range(0,len(a)):
        b[(arrayLen+i-d)%arrayLen] = a[i]
    return b
if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(' '.join(map(str, result)))
