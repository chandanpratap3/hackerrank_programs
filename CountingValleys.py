#!/bin/python3

#==============================================RULER==================================================#
#--------10--------20--------30--------40--------50--------60--------70--------80--------90--------100#
#=====================================================================================================#
#Title 		: Counting Valleys
#Problem 	: An avid hiker keeps meticulous records of their hikes. During the last hike that took
#			  exactly  steps, for every step it was noted if it was an uphill,U, or a downhill,D step.
#			  Hikes always start and end at sea level, and each step up or down represents a 1 unit 
#			  change in altitude. We define the following terms:
#			  
#			  * A mountain is a sequence of consecutive steps above sea level, starting with a step up
#			  from sea level and ending with a step down to sea level.
#			  
#			  * A valley is a sequence of consecutive steps below sea level, starting with a step down
#			  from sea level and ending with a step up to sea level.
#			  
#			  Given the sequence of up and down steps during a hike, find and print the number of
#			  valleys walked through.
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

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

def countingValleys(steps, path):
    level = 0
    count = 0

    for i in range(steps):
        if path[i] == "U":
            level += 1
            if level == 0:
                count += 1

        else:
            level -= 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
