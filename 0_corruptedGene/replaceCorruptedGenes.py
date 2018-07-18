# -*- coding: utf-8 -*-
"""
This file replaces all corrupted genes in the original ST_data

Created on Wed Jun 27 15:51:03 2018

@author: fuqixu
"""
import csv
# csv package can read large csv files line by line
import os
import sys
import re
import pandas
import pandas

rawFile = sys.argv[1]
# sys.argv[2] = refFile

# Get corresponding corrupted gene list
sample = re.compile(r'\d.\d')
sampleID = sample.findall(str(rawFile))[0]
refName = 'object' + str(sampleID) + '.csv'

refFile = os.getcwd() + '/corruptedGeneSymbols/' + refName
outFile = os.getcwd()
with open(refFile, 'r') as ref:
    geneDict = {}
    for lines in ref:
        geneList = lines.strip().split(',')
        # list[1]: old name, list[0]: new name
        geneDict.update({geneList[1]: geneList[0]})

# Load the file to be processed.
# Read file to replace
count = 0
with open(rawFile, 'r') as raw:
    rawReader = csv.reader(raw)
    newRows = []
    for row in rawReader:
        temp = []
        for rowi in row:
                for key, value in geneDict.items():
                    if key in rowi:
                        rowi = rowi.replace(key, value)
                        count = count + 1
                temp.append(rowi)
        newRows.append(temp)

newDf = pandas.DataFrame(newRows)
outName = str(rawFile)+'_'
newDf.to_csv(outName,header = False)
print(str(len(geneDict)) + ' genes in the dict\n')
print( str(count) + " replacements")
