#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    arr = a
    l = len(arr)
    swaps = 0
    for i in range(l):
        for j in range(l-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaps += 1

    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(arr[0]))
    print('Last Element: {}'.format(arr[l-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
