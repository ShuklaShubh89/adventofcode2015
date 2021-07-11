
num = '1321131112'
strnum = list(num)
counter=1

def lookandsay(num: list) -> list:
        resultlist=[]
        counter=1
        for x in range(len(num)-1):
            if(num[x]!=num[x+1]):
                resultlist.append(str(counter))
                resultlist.append(num[x])
                counter=1
            elif(num[x]==num[x+1]):
                counter+=1
                continue
        resultlist.append(str(counter))
        resultlist.append(num[-1])
        return resultlist

for x in range(50):
    print(x, len(strnum))
    strnum = lookandsay(strnum)
print(len(strnum))