#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribe = 0
    lenq = len(q)
    for i in range(lenq-1,-1,-1):
        if (q[i] - (i + 1) > 2):
            return 'Too chaotic'
        j = max(0, q[i] - 2)
        for k in range(j,i):
            if (q[k] > q[i]):
                bribe+=1

    return bribe


if __name__ == '__main__':
    t = int(input())
    output =[]
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        output.append(minimumBribes(q))
    print(*output , sep = "\n")
