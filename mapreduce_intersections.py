#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: MapReduce Patterns - Intersections
Problem 	: Given two sets of integers, R and S select and display the interesection. The relative ordering of integers in the intersecting set should be same as that in set R.

            Sample Input:
            10 10
			-51
			-43
			74
			-96
			24
			-14
			11
			77
			-45
			-90
			45
			8
			29
			0
			-43
			-13
			-72
			71
			-96
			-26
            Sample Output:
			-43
			-96
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
        self.set1 = []
        self.set2 = []

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
        
        for val in self.set1:
            if val in self.set2:
                self.emit(val)

        return self.result

mapReducer = MapReduce()

def mapper(record):
    key = record["key"]
    value = record["value"]
    mapReducer.emitIntermediate(key, value)

def reducer(key, list_of_values):
    
    if key == "R":
        mapReducer.set1 = list_of_values
    else:
        mapReducer.set2 = list_of_values


if __name__ == '__main__':
  inputData = []
  final_result = []
  nr, ns = map(int, raw_input().split())
  for i in range(nr):
    k = int(raw_input())
    inputData.append(json.dumps({"key":"R","value":k}))
  for i in range(ns):
    k = int(raw_input())
    inputData.append(json.dumps({"key":"S","value":k}))

  result = mapReducer.execute(inputData, mapper, reducer)
  for n in result:
    if n not in final_result:
        print(n)
        final_result.append(n)
