#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: MapReduce Patterns - Selection
Problem 	: Given two sets of integers, R and S select and display the interesection. The relative ordering of integers in the intersecting set should be same as that in set R.

            Sample Input:
            10
			99
			43
			-27
			21
			99
			-100
			35
			-91
			-45
			59
            Sample Output:
			99
			43
			21
			99
			35
			59
Developer	: Chandan Pratap

Date            Version     Modified By             Reason for Modification
----------      -------     --------------------    -----------------------------------------------
12/26/2020      1.0         chandanpratap3          Initial Version
"""

import json
import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
        self.final_list = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        for item in self.result:
            if item not in self.final_list:
              print item.split()[0]
              self.final_list.append(item)

mapReducer = MapReduce()

def mapper(record):
    value = record["value"]
    # ADD THE REQUIRED LOGIC BELOW
    # You may need to add some lines for the mapper logic to work
    # At the end, you need to complete the emit intermediate step
    if int(value) % 2 != 0:
        mapReducer.emitIntermediate("odd", value)

def reducer(key, list_of_values):
    # ADD THE REQUIRED LOGIC BELOW
    # You may need to add some lines for the reducer logic to work
    # At the end, you need to complete the emit step
    for val in list_of_values:
      if int(val) > 10:
        mapReducer.emit(val)


if __name__ == '__main__':
  inputData = []
  counter = 0
  for line in sys.stdin:
   counter += 1
   if counter != 1:
     inputData.append(json.dumps({"key":counter,"value":line}))
  mapReducer.execute(inputData, mapper, reducer)
  