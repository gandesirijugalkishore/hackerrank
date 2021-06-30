#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here 
    y=[]
    cntr=0
    m=list(set(ar))
    for i in m:
        if ar.count(i) %2==0:
            cntr+=ar.count(i)/2
        elif ar.count(i) >2:
            cntr+=ar.count(i)//2
                            
    return int(cntr)
                
                       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
