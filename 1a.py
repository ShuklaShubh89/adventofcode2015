brackets = input().strip()

brackets = list(brackets)

floor=0
for x in brackets:
    if(x == ')'):
        floor-=1
    elif(x == '('):
        floor+=1

print(floor)