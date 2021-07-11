from collections import defaultdict

def def_value():
    return 0

directions = input()
directionlist = list(directions)
coordinates1 = [0,0]
coordinates2 = [0,0]
housevisits1 = defaultdict(def_value)
housevisits2 = defaultdict(def_value)

for x in range(len(directionlist)):
    if(x%2 == 0):
        if(directionlist[x] == '^'):
            coordinates1[1]+=1
        elif(directionlist[x] == 'v'):
            coordinates1[1]-=1
        elif(directionlist[x] == '>'):
            coordinates1[0]+=1
        elif(directionlist[x] == '<'):
            coordinates1[0]-=1
        housevisits1[str(coordinates1)]+=1
    else:
        if(directionlist[x] == '^'):
            coordinates2[1]+=1
        elif(directionlist[x] == 'v'):
            coordinates2[1]-=1
        elif(directionlist[x] == '>'):
            coordinates2[0]+=1
        elif(directionlist[x] == '<'):
            coordinates2[0]-=1
        housevisits2[str(coordinates2)]+=1

housevisits3 = {}

for x,y in housevisits1.items():
    if(x in list(housevisits2.keys())):
        housevisits3[x] = y+int(housevisits2.get(x))
    else:
        housevisits3[x] = y

for x,y in housevisits2.items():
    if(x not in list(housevisits1.keys())):
        housevisits3[x] = y

resultcounter=0
for x in list(housevisits3.values()):
    if (x>=1):
        resultcounter+=1
    else:
        continue

print(resultcounter)
