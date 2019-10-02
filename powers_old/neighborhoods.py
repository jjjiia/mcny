##make dictionaries for all columns
import csv
import json
import collections

def getNameCoord():
    neighborhoods = []
    with open("zillow-neighborhoods.json") as inputFile:
        data = json.load(inputFile)
        for i in data:
            if "geometry" not in i.keys():
                print i
                print
            else:
                name = i["fields"]["name"]
                point = i["geometry"]["coordinates"]
                lat = point[0]
                lng = point[1]
                print {"city":"New York","latitude":lat,"longitude":lng,"name":name}
                neighborhoods.append({"city":"New York","latitude":lat,"longitude":lng,"name":name})
        #print neighborhoods

    
getNameCoord()

#wordSearchCount()