from collections import defaultdict

def def_value():
    return 0

directions = input()
directionlist = list(directions)
coordinates = [0,0]
housevisits = defaultdict(def_value)

for x in directionlist:
    if(x == '^'):
        coordinates[1]+=1
    elif(x == 'v'):
        coordinates[1]-=1
    elif(x == '>'):
        coordinates[0]+=1
    elif(x == '<'):
        coordinates[0]-=1
    #print(str(coordinates))
    housevisits[str(coordinates)]+=1

resultcounter=1 #because 0,0 is also a house
for x in list(housevisits.values()):
    #print(x)
    if (x>=1):
        resultcounter+=1
    else:
        continue

print(resultcounter)

