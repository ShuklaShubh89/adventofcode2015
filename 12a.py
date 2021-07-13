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
            sum+=x
    return sum

def traverse(enjson):
    global total
    if(type(enjson)==list):
        total+=getlistsum(enjson)
        print(total)
        for x in enjson:
            if(type(x)==list):
                traverse(x)
            elif(type(x)==dict):
                traverse(list(x.values()))
    return total

total=0
print(traverse(encodedjson))
