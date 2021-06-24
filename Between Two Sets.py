#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    x = []
    y = []
    for i in a:
        x_i = [n*i for n in range(1000)]
        x.append(x_i)
    r = set(x[0])  
    for s in x[1:]:
        r.intersection_update(s)
    r=sorted(list(r))
    for i in b:
        y_i = [j for j in r if j>0 and i%j == 0]
        y.append(y_i)

    w=set(y[0])
    for k in y[1:]:
        w.intersection_update(set(k))
    return(len(w))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
