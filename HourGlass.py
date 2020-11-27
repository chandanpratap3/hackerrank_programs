#!/bin/python3

#==============================================RULER==================================================#
#--------10--------20--------30--------40--------50--------60--------70--------80--------90--------100#
#=====================================================================================================#
#Title 		: Hour Glass 2D Array - DS
#Problem 	: Given a 6x6 2D Array, arr:
#
#               1 1 1 0 0 0
#               0 1 0 0 0 0
#               1 1 1 0 0 0
#               0 0 0 0 0 0
#               0 0 0 0 0 0
#               0 0 0 0 0 0
#
#               An hourglass in A is a subset of values with indices falling in this pattern in arr's
#               graphical representation:
#               a b c
#                 d
#               e f g
#
#             There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values.
#             Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass
#             sum. The #array will always be 6 x 6.
#
#Developer	: Chandan Pratap
#
#Date			Version		Modified By				Reason for Modification
#----------		-------		--------------------	--------------------------------------------------#
#11/26/2020		1.0			chandanpratap3			Initial Version
#=====================================================================================================#

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    i = 0
    j = 0
    max_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

    
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hg_sum = 0
            hg_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]+ arr[i+2][j]+ arr[i+2][j+1]+ arr[i+2][j+2]

            if max_sum < hg_sum:
                max_sum = hg_sum

    return max_sum

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
