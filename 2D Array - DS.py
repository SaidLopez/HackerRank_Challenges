#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    block = []
        
    def sum_matrix(x,y):
        a=0
        for i in range(3):
            for j in range(3):
                if (i == 1 and j == 0) or (i==1 and j==2):
                    pass
                else:    
                    a += arr[i+x][j+y]
        return a 
    
    for i in range(4):
        for j in range(4):
            block.append(sum_matrix(i,j))
    
    return max(block)
            
            
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
