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
    ribbonreq = (l*w*h) + 2*(listlwh[0]+listlwh[1])
    total+=ribbonreq

print(total)