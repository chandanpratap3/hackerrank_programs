#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: Map Reduce Advanced - Relational Join
Problem 	: The input is a number of lines with records from two tables Employee and Department. A tuple from Employee table will look like:
			Employee [Person_Name] [SSN]
            A tuple from Department table will look like:
            Department [SSN] [Department_Name]
            
			The required output is to print the JOIN of the two tables Employee and Department, in the format shown.
            Sample Input:
            Department,1234,Sales
            Employee,Susan,1234
            Department,1233,Marketing
            Employee,Joe,1233
            Department,1233,Accounts
            
            Sample Output:
            ('1233', 'Joe', 'Accounts')
            ('1233', 'Joe', 'Marketing')
            ('1234', 'Susan', 'Sales')
Developer	: Chandan Pratap

Date            Version     Modified By             Reason for Modification
----------      -------     --------------------    -----------------------------------------------
12/26/2020      1.0         chandanpratap3          Initial Version
"""

import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])
        
        self.result.sort()
        for item in self.result:
            print(item)

mapReducer = MapReduce()

def mapper(record):
    t, v1, v2 = record.strip().split(",")

    if t == "Employee":
        mapReducer.emitIntermediate(v2,("P", v1))
    else:
        mapReducer.emitIntermediate(v1,("D", v2))

def reducer(key, list_of_values):
    list_of_values = set(list_of_values)
    list_of_values = sorted(list(list_of_values))
    person_name = list_of_values[-1][-1]
    
    for D in list_of_values:
        if D[0] == "D":
            mapReducer.emit((key, person_name, D[1]))

if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)
