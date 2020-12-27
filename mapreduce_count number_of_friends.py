#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: Map Reduce Advanced - Count number of friends
Problem 	: The input is a number of lines with pairs of name of friends, in the form:
			[Friend1] [Friend2]
			The required output is to print the number of friends of each person
            Sample Input:
            Joe Sue
            Sue Phi
            Phi Joe
            Phi Alice
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
            print("{\"key\":\""+item[0]+"\",\"value\":\"" + str(item[1]) + "\"}")

mapReducer = MapReduce()

def mapper(record):
    record = record.strip().split() #"/t", 1)
    for person in record:
        mapReducer.emitIntermediate(person, 1)

def reducer(key, list_of_values):
    mapReducer.emit([key, len(list_of_values)])

if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)
  