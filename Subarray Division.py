#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    a=0     #1
    b=a+m  #3
    cntr=0
    for i in range(len(s)):
        b=a+m
        print("a,b",a,b)
        if b<=(len(s)):
            if sum(s[a:b])==d:
#                 print("sum(s[a:b]---->{},d-------->{}".format(sum(s[a:b]),d))
                cntr+=1
                a+=1
#                 b+=1
            else:
                a+=1
#                 b+=1
#         else:
#             print("no")
    return cntr
            
        
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
