#!/bin/python3

import math
import os
import random
import re
import sys

def activityNotifications(expenditure, d):

    notif = 0 ; MAX = 200 ; c = [0] * (MAX+1)
    for e in expenditure[:d] : c[e] += 1
    #print(c)
    def median():
        s = 0
        for x in range(MAX+1):
            s += c[x]
            if 2*s >= d : break
        if d%2 == 1 or 2*s > d : return x

        for y in range(x+1,MAX+1):
            if c[y] != 0 : break
        return (x+y)/2

    for i in range(d,len(expenditure)):
        #print(c)
        if expenditure[i] >= 2*median() : notif += 1
        c[expenditure[i-d]] -= 1
        c[expenditure[i]] += 1
    return notif

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result))