import sys
import itertools

def find_distance(city1, city2):
    distance=0
    try:
        distance = distances[city1,city2]
    except KeyError:
        distance = distances[city2,city1]
    return distance

strings = sys.stdin.readlines()
distances={}
cities=[]
for x in strings:
    xlist = x.split()
    distances[xlist[0], xlist[2]] = int(xlist[4])
    cities.append(xlist[0])
    cities.append(xlist[2])


cities = list(set(cities))
paths=[[]]
paths = list(itertools.permutations(cities))

resultdist=[]
for path in paths:
    print(path)
    totaldistance=0
    for city in range(len(path)-1):
        print(path[city],path[city+1])
        totaldistance+=find_distance(path[city],path[city+1])
    print(totaldistance)
    resultdist.append(totaldistance)

resultdist.sort(reverse=True)
print(resultdist[0])