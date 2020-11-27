#!/bin/python3

#==============================================RULER==================================================#
#--------10--------20--------30--------40--------50--------60--------70--------80--------90--------100#
#=====================================================================================================#
#Title 		: New year Chaos
#Problem 	: It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There
#			  are a number of people queued up, and each person wears a sticker indicating their
#			  initial position in the queue. Initial positions increment by 1 from 1 at the front of
#			  the line to n at the back.
#			  
#			  Any person in the queue can bribe the person directly in front of them to swap
#			  positions. If two people swap positions, they still wear the same sticker denoting their
#			  original places in line. One person can bribe at most two others. For example, if n=8
#			  and Person 5 bribes Person 4, the queue will look like this: 1,2,3,5,4,6,7,8.
#			  
#			  Fascinated by this chaotic queue, you decide you must know the minimum number of bribes
#			  that took place to get the queue into its current state!
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

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    valid = True
    for i in reversed(range(len(q))):
        v = i + 1
        if q[-1] == v:
            q.pop(-1)
        elif len(q) > 1 and q[-2] == v:
            q.pop(-2)
            bribes += 1
        elif len(q) > 2 and q[-3] == v:
            q.pop(-3)
            bribes += 2
        else:
            valid = False
            break
    if valid:
        print(bribes)
    else:
        print("Too chaotic")

    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
