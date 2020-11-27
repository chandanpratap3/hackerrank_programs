#!/bin/python3

#==============================================RULER==================================================#
#--------10--------20--------30--------40--------50--------60--------70--------80--------90--------100#
#=====================================================================================================#
#Title 		: Sales by Match
#Problem 	: Alex works at a clothing store. There is a large pile of socks that must be paired by 
#			  color for sale. Given an array of integers representing the color of each sock,
#			  determine how many pairs of socks with matching colors there are.
#Developer	: Chandan Pratap
#
#Date			Version		Modified By				Reason for Modification
#----------		-------		--------------------	--------------------------------------------------#
#11/25/2020		1.0			chandanpratap3			Initial Version
#=====================================================================================================#


import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    checked = []
    count = 0
    pairs = 0

    for i in range(n):
        if ar[i] in checked:
            print("{} is already in {}".format(ar[i], checked))
        else:
            print("{} is not in {}".format(ar[i], checked))

            count = 0
            for j in range(i, n):
                if ar[i] == ar[j]:
                    count += 1

            pairs += int(count/2)
            checked.append(ar[i])

    return pairs 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
