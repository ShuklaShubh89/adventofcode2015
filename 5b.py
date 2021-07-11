import sys


strings = sys.stdin.readlines()
total = 0
for x in strings:
    xlist = list(x)
    condition1=False
    condition2=False
    for y in range(len(xlist)-1):
        for z in range(y+2,len(xlist)-1):
            if(xlist[y]+xlist[y+1]==xlist[z]+xlist[z+1]):
                condition1=True
    for y in range(len(xlist)-2):
        if(xlist[y]==xlist[y+2]):
            condition2=True
    if(condition1==True and condition2==True):
        total+=1

print(total)
