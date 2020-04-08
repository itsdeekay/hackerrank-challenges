#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    ground = 0
    temp = 0
    numberOfValleys = 0
    for i in range(0,len(s)):
        temp = ground
        ground = ground+1 if s[i]=='U' else ground-1
        if(temp<0 and ground==0):
            numberOfValleys +=1

    return numberOfValleys
if __name__ == '__main__':
   
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result) + '\n')
