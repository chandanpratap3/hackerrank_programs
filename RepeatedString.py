#!/bin/python3

#==============================================RULER==================================================#
#--------10--------20--------30--------40--------50--------60--------70--------80--------90--------100#
#=====================================================================================================#
#Title 		: Repeated String
#Problem 	: Lilah has a string, s, of lowercase English letters that she repeated infinitely many
#			  times.
#
#			  Given an integer, n, find and print the number of letter a's in the first n letters of
#			  Lilah's infinite string.
#			  For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac,
#			  the first 10 characters of her infinite string. There are 4 occurrences of a in the
#			  substring.
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

# Complete the repeatedString function below.
def repeatedString(s, n):
    rem = n % len(s)
    count = 0
    
    for pos in range(len(s)):
        if s[pos] == "a":
            count += 1
    
    count = count* (int(n/len(s)))
            
    for pos in range(rem):
        if s[pos] == "a":
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
