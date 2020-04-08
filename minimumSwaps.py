#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ans =0 
    for i in range(len(arr)): 
        while(arr[i] != i+1): 
            temp = arr[i]
            arr[i] = arr[temp-1]
            arr[temp-1] = temp
            ans += 1
    return ans 
if __name__ == '__main__':
    
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(str(res))

