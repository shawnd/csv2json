
# Converts csv file to json
# @author Per-Henrik Kvalnes

import sys
import json
import argparse

parser = argparse.ArgumentParser(description='csv filename')
parser.add_argument('csv')
args = parser.parse_args()
inFileName = args.csv
infile = open(inFileName)
outfile = open(inFileName.replace(".csv", "")+".json", "w")

first = 0
header = {}

jsonList = []

for line in infile:

    # if first time, prepare the header 
    if not first:
        line = line.strip("\n")
        keys = line.split(";")

        i = 0
        for key in keys:
            if key != "":
                header[i] = key
                i += 1



        first = 1

    # if noe, make an json object
    else:
        obj = {}
        line = line.strip("\n")
        values = line.split(";")

        i = 0
        for value in values:
            if value != "":
                obj[header[i]] = value

                i += 1

        jsonList.append(obj)

jsonString = json.dumps(jsonList, indent=4)

outfile.write(jsonString)
outfile.close()
