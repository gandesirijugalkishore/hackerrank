#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    h = scores[0]
    l = scores[0]
    c_h = 0
    c_l = 0
    for i in range(1,len(scores)):
        if scores[i] >h and scores[i] >l :
            h=scores[i]
            c_h +=1
        elif scores[i] <h and scores[i] <l:
            l = scores[i]
            c_l +=1
    return c_h,c_l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
