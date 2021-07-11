import sys

dimensions = sys.stdin.readlines()
total = 0
for x in dimensions:
    x.strip()
    lwh = x.split("x")
    l = int(lwh[0])
    w = int(lwh[1])
    h = int(lwh[2])
    listlwh = [l,w,h]
    listlwh.sort()
    paperreq = (2*l*w) + (2*w*h) + (2*h*l) + listlwh[0]*listlwh[1]
    total+=paperreq

print(total)


