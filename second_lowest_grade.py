#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: Second Lowest Grade
Problem 	: Print out the names of students in alphabetic order who got second lowest grades.

Developer	: Chandan Pratap

Date            Version     Modified By             Reason for Modification
----------      -------     --------------------    -----------------------------------------------
11/28/2020      1.0         chandanpratap3          Initial Version
"""

if __name__ == '__main__':
    marks = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append([name, score])
        scores.add(score)

    second_score = sorted(list(scores))[1]
    print('\n'.join(n for n, s in sorted(marks) if s == second_score))
