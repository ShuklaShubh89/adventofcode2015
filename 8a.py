import sys

strings = sys.stdin.readlines()
actualchars = 0
inmemchar = 0
for x in strings:
    xlist = list(x.strip())
    print(xlist)
    actualchars+=len(xlist)
    inmemlist=[]
    y=1
    while (y<len(xlist)-1):
        inmemlist.append(xlist[y])
        if(xlist[y]=='\\' and xlist[y+1]=='\"'):
            y+=1
        elif(xlist[y]=='\\' and xlist[y+1]=='\\'):
            y+=1
        elif(xlist[y]=='\\' and xlist[y+1]=='x'):
            y+=3
        y+=1
    print(inmemlist)
    inmemchar+=len(inmemlist)
print(actualchars)
print(inmemchar)
print(actualchars-inmemchar)

