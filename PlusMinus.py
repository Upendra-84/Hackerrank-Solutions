#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for items in arr:
        if items>0:
            p = p +1
        elif items<0:
            n = n+1
        elif items==0:
            z = z+1
    a = float(p/len(arr))
    b = float(n/len(arr))
    c = float(z/len(arr))
    return print(a,b,c,sep='\n')



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
