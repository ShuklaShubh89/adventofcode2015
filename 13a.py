import sys
import itertools

strings = sys.stdin.readlines()
neighbour = []
person = []
dictneighbours={}
resulthappiness = []

def calculateHappiness(seatingorder):
    for persons in seatingorder:
        totalhappiness=0
        for y in range(len(persons)):
            if(y==len(persons)-1):
                temppair = dictneighbours[persons[y], persons[0]]
                temppair2 = dictneighbours[persons[0], persons[y]]
            else:
                temppair = dictneighbours[persons[y], persons[y+1]]
                temppair2 = dictneighbours[persons[y+1], persons[y]]
            if(temppair[0]=='gain'):
                totalhappiness+= temppair[1]
            elif(temppair[0]=='lose'):
                totalhappiness-= temppair[1]
            if(temppair2[0]=='gain'):
                totalhappiness+= temppair2[1]
            elif(temppair2[0]=='lose'):
                totalhappiness-= temppair2[1]
        resulthappiness.append(totalhappiness)

for x in strings:
    sentence = x.split()
    person.append(sentence[0])
    hunits = int(sentence[3])
    happiness = sentence[2]
    dictneighbours[sentence[0],sentence[10].split('.')[0]] = [happiness,hunits]

personpermutations = itertools.permutations(set(person))
calculateHappiness(personpermutations)
print(max(resulthappiness))
