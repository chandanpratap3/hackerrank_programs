#!/bin/python3

"""
RULER----10--------20--------30--------40--------50--------60--------70--------80--------90--------100
Title 		: Map Reduce Tutorials - #3 Composite Keys
Problem 	: The given input has a number of rows, each with four fields from a table, containing:
			Country, State, City, Population of the city
            You are required to output:
            Country, State, Population of the state (obtained by summing up the population of each city in that state)
            
            Sample Input:
            India   Tamil Nadu  Chennai 4.344
			India   Maharashtra Mumbai  11.98
			India   Maharashtra Pune    2.538
			India   Tamil Nadu  Coimbatore  0.931
			USA Washington  Seattle 0.652
			USA Washington  Tacoma  0.20
            
            Sample Output:
			{"key":"India,Tamil Nadu","value":5}
			{"key":"India,Maharashtra","value":15}
			{"key":"USA,Washington","value":1}
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

        jenc = json.JSONEncoder()
        for item in self.result:
            print("{\"key\":\""+item[0]+"\",\"value\":" + str(item[1]) + "}")

mapReducer = MapReduce()

def mapper(record):
    key = record["key"]
    value = record["value"]
    mapReducer.emitIntermediate(key, value)

def reducer(key, list_of_values):
    sum1 = 0.0
    for value in list_of_values:
      sum1 += float(value)
    mapReducer.emit((key,int(round(sum1))))


if __name__ == '__main__':
  inputData = []
  counter = 0
  for line in sys.stdin:
   counter += 1
   country, state, city, population = line.strip().split("\t")
   inputData.append(json.dumps({"key":country+","+state,"value":population}))
  mapReducer.execute(inputData, mapper, reducer)
  