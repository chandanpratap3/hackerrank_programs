#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title		: Arrays Left Rotation
Problem 	: A left rotation operation on an array shifts each of the array's elements 1 unit to the
            left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the
            array would become [3,4,5,1,2].

            Given an array a of n integers and a number, d, perform d left rotations on the array.
            Return the updated array to be printed as a single line of space-separated integers.
Developer	: Chandan Pratap

Date            Version     Modified By             Reason for Modification
----------      -------     --------------------    -----------------------------------------------
11/27/2020      1.0         chandanpratap3          Initial Version
"""

import math
import os
import random
import re
import sys

def rotLeft(a, d):
    temp = a[0]

    for j in range(d):
        temp = a[0]
        a.pop(0)
        a.append(temp)

    return a
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
