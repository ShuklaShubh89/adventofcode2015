import json
import sys

inputjson = sys.stdin.read()
encodedjson = json.loads(inputjson)

def getlistsum(listnum) -> int:
    sum=0
    for x in listnum:
        if(type(x)==int):
            sum+=x
    return sum 

def getdictsum(dictnum) -> int:
    sum=0
    for x in list(dictnum.values()):
        if(type(x)==int):
            print(sum)
            sum+=x
    return sum

def traverse(enjson):
    global total
    if(type(enjson)==list):
        total+=getlistsum(enjson)
        for x in enjson:
            if(type(x)==list or type(x)==dict):
                traverse(x)
    elif(type(enjson)==dict and 'red' in list(enjson.values())):
        return total
    elif(type(enjson)==dict):
        total+=getdictsum(enjson)
        for x in list(enjson.values()):
            if(type(x)==list or type(x)==dict):
                traverse(x)
    return total

total=0
print(traverse(encodedjson))
