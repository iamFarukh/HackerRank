import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, arr):
# CODE BY MOHAMMAD FARUKH 
    c = n/2
    # To store the required count  
    count = 0;  
    # Sort the original array  
    arr.sort(); 
    i = 0; 
    while i < (n-1) :
        if (count<=c):
            # A valid pair is found  
            if (arr[i] == arr[i + 1]) : 
                count += 1;  
    
                # Skip the elements of  
                # the current pair  
                i = i + 2;  
    
            # Current elements doesn't make  
            # a valid pair with any other element  
            else : 
                i += 1;  
  
    return count;
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
