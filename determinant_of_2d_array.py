#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: Determinant of an Array (Algebra)
Problem 	: You are given a square matrix A with dimensions N X N. Your task is to find the
			determinant. Note: Round the answer to 2 places after the decimal.

Date            Version     Modified By             Reason for Modification
----------      -------     --------------------    -----------------------------------------------
11/28/2020      1.0         chandanpratap3          Initial Version
"""

import numpy

if __name__ == '__main__':
    size = int(input())
    array_items = []
    
    for _ in range(size):
        line = map(float, input().strip().split())
        array_items.append(list(line))
        
    print(round(numpy.linalg.det(array_items), 2))
