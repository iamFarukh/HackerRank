import math
import os
import random
import re
import sys

# 6  0 1 2 3 4 5 
# a [0 0 0 0 1 0]

# i = 0 ; 2>=6 or 0 == 1  ==> (false) i = 0+2 = 2 ==> ans = 1
# i = 2 ; 4>=6 or 1 == 1  ==> (true)  i = 2+1 = 3 ==> ans = 2
# i = 3 ; 5>=6 or 0 == 1  ==> (false) i = 3+2 = 5 ==> ans = 3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):
    ans = 0
    i = 0
    while i<(n-1):
        if (i+2>=n or c[i+2]==1):
            ans+=1
            i+=1
        else:
            ans+=1
            i+=2
    return ans

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(n,c)
    print(result)
