#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: List Comprehensions
Problem 	: You are given three integers x,y and z representing the dimensions of a cuboid along
            with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D
            grid where the sum of i+j+k is not equal to n. Here, 1<=i<=x;1<=j<=y;1<=k<=z. 
            Use list comprehensions rather than multiple loops.

Developer	: Chandan Pratap

Date            Version     Modified By             Reason for Modification
----------      -------     --------------------    -----------------------------------------------
11/27/2020      1.0         chandanpratap3          Initial Version
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])
