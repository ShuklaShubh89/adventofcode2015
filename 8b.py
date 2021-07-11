import sys

strings = sys.stdin.readlines()
actualchars = 0
inmemchar = 0
for x in strings:
    xlist = list(x.strip())
    print(xlist)
    actualchars+=len(xlist)
    inmemcount=0
    for y in range(len(xlist)):
        if(xlist[y]=='\\'):
            inmemcount+=1
        elif(xlist[y]=='\"'):
            inmemcount+=1
        inmemcount+=1
    print(inmemcount)
    inmemchar+=inmemcount+2
print(actualchars)
print(inmemchar)
print(inmemchar-actualchars)

