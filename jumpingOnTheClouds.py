#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count =0
    i=0
    while(i<len(c)-3):
        if c[i+2] == 0:
            i = i+2
            count+=1
            continue
        if c[i+1] == 0:
            i = i+1
            count+=1
            continue
        else:
            break
    count += 1
    return count

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result))
