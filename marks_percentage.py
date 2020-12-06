#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: Finding student's percentage
Problem 	: Read in a dictionary containing key/value pairs of name:[marks] for a list of
			students. Print the average of the marks array for the student name provided,
			showing 2 places after the decimal.
Developer	: Chandan Pratap

Date            Version     Modified By             Reason for Modification
----------      -------     --------------------    -----------------------------------------------
11/28/2020      1.0         chandanpratap3          Initial Version
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(format(sum(student_marks[query_name])/len(student_marks[query_name]), '.2f'))
    