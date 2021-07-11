import sys


strings = sys.stdin.readlines()
total = 0
for x in strings:
    xlist = list(x)
    vowels = ['a','e','i','o','u']
    notrequired = ['ab','cd','pq','xy']
    vowelcounter=0
    condition2=False
    condition3=True
    for y in range(len(xlist)-1):
        if(xlist[y]==xlist[y+1]):
            condition2=True
        if(xlist[y] in vowels):
            vowelcounter+=1
        if(xlist[y]+xlist[y+1] in notrequired):
            condition3=False
    if(vowelcounter>=3 and condition2==True and condition3==True):
        total+=1

print(total)
