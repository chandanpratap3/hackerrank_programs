#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: Runner-Up Score
Problem 	: Given the participants' score sheet for your University Sports Day, you are required
			to find the runner-up score. You are given n scores. Store them in a list and find the
			score of the runner-up.
Developer	: Chandan Pratap

Date            Version     Modified By             Reason for Modification
----------      -------     --------------------    -----------------------------------------------
11/27/2020      1.0         chandanpratap3          Initial Version
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = set(arr)
    
    if len(arr) > 1:
        print(sorted(list(arr))[-2])
    