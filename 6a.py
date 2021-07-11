import sys
from collections import defaultdict

def def_value():
    return '0'

dictlights = defaultdict(def_value)

strings = sys.stdin.readlines()
for x in strings:
    xlist = x.split()
    if(xlist[0]=='toggle'):
        operation = xlist[0]
        coordinate1 = xlist[1]
        coordinate2 = xlist[3]
    else:
        operation = xlist[1]
        coordinate1 = xlist[2]
        coordinate2 = xlist[4]
    xcoordinate1 = int(coordinate1.split(',')[0])
    ycoordinate1 = int(coordinate1.split(',')[1])
    xcoordinate2 = int(coordinate2.split(',')[0])
    ycoordinate2 = int(coordinate2.split(',')[1])
    #print('cood1', xcoordinate1,ycoordinate1)
    #print('cood2', xcoordinate2,ycoordinate2)
    for y in range(xcoordinate1, xcoordinate2+1):
        for z in range(ycoordinate1, ycoordinate2+1):
            if(operation=='toggle'):
                if(dictlights[str(y)+str(z)]=='1'):
                    dictlights[str(y)+str(z)] = '0'
                else:
                    dictlights[str(y)+str(z)] = '1'
            elif(operation=='on' and dictlights[str(y)+str(z)]=='0'):
                    dictlights[str(y)+str(z)] = '1'
            elif(operation=='off' and dictlights[str(y)+str(z)]=='1'):
                    dictlights[str(y)+str(z)] = '0'
                    
print(list(dictlights.values()).count('1'))
