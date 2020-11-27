#!/bin/python3

#==============================================RULER==================================================#
#--------10--------20--------30--------40--------50--------60--------70--------80--------90--------100#
#=====================================================================================================#
#Title 		: Jumping On The Clouds
#Problem 	: Emma is playing a new mobile game that starts with consecutively numbered clouds. Some
#			  of the clouds are thunderheads and others are cumulus. She can jump on any cumulus
#			  cloud having a number that is equal to the number of the current cloud plus 1 or 2. She
#			  must avoid the thunderheads. 
#			  Determine the minimum number of jumps it will take Emma to jump from her starting
#			  postion to the last cloud. It is always possible to win the game.
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


def jumpingOnClouds(c):
    steps = 0
    i = 0

    while i < (len(c) - 1):
        if i == len(c) - 2:
            i += 1
            steps += 1

        elif c[i + 2] == 0:
            i += 2
            steps += 1

        else:
            i += 1
            steps += 1

    return steps
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
