
brackets = input().strip()

brackets = list(brackets)

floor=0
for x in range(len(brackets)):
    if(brackets[x] == ')'):
        floor-=1
    elif(brackets[x] == '('):
        floor+=1
    if(floor==-1):
        print(x+1)
        break
