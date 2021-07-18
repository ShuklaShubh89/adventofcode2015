import sys
from collections import defaultdict

def addpoints(reindeernames,secs):
    for x in reindeernames:
        reindeerprops = reindeers[x]
        if(secs%(int(reindeerprops[1])+int(reindeerprops[2]))<=(int(reindeerprops[1]))):
            distancetravelled[x]+=int(reindeerprops[0])
        if(distancetravelled[x]==max(list(distancetravelled.values()))):
            pointsdict[x]+=1


def defaultdistance():
    return 0

strings = sys.stdin.readlines()
flightinfo = []
reindeers = {}
distancetravelled= defaultdict(defaultdistance)
pointsdict = defaultdict(defaultdistance)
for x in strings:
    sentence = x.split()
    flightinfo.append(sentence[3])
    flightinfo.append(sentence[6])
    flightinfo.append(sentence[13])
    reindeers[sentence[0]] = list(flightinfo)
    flightinfo.clear()

timeinsecs = 2503
for x in range(1, timeinsecs+1):
    addpoints(list(reindeers.keys()),x)

print*
print(max(list(pointsdict.values())))
