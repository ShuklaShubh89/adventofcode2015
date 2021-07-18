import sys

def calculatedistance(reindeername):
    totaldistance = 0
    reindeerprops = reindeers[reindeername]
    totalstretches = int(2503/(int(reindeerprops[1])+int(reindeerprops[2])))
    totaldistance+=totalstretches*(int(reindeerprops[0])*int(reindeerprops[1]))
    laststretch = int(2503%(int(reindeerprops[1])+int(reindeerprops[2])))
    if(laststretch<=int(reindeerprops[1])):
        totaldistance+=laststretch*(int(reindeerprops[0]))
    else:
        totaldistance+=int(reindeerprops[0])*int(reindeerprops[1])
    return totaldistance

strings = sys.stdin.readlines()
flightinfo = []
reindeers = {}

for x in strings:
    sentence = x.split()
    flightinfo.append(sentence[3])
    flightinfo.append(sentence[6])
    flightinfo.append(sentence[13])
    reindeers[sentence[0]] = list(flightinfo)
    flightinfo.clear()

timeinsecs = 2503
print(list(reindeers.keys()))
print(max(map(calculatedistance,list(reindeers.keys()))))
for x in map(calculatedistance,list(reindeers.keys())):
    print(x)