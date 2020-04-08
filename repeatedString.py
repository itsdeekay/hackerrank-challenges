#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    countOfa = s.count('a')
    lengthOfs = len(s)
    occuranceOfa = (n//lengthOfs )* countOfa
    if n%lengthOfs !=0:
        occuranceOfa += s[:n%lengthOfs].count('a')
    return occuranceOfa

if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result))

