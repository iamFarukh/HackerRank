import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    vally = 0
    prev_height = 0
    for i in s:
        if i =="U":
            count+=1
        elif i == "D":
            count-=1
        # print(count)
        if count == 0 and prev_height < 0:
            vally +=1
        prev_height = count
        
    return vally

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print (result)