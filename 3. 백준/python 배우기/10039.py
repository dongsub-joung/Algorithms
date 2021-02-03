def adjustScore(score:int)->int:
    if score>=40:
        return score
    elif score<40:
        score=40
        return score

onesub= int(input())
sehi= int(input())
sangoun= int(input())
sumi= int(input())
gansu= int(input())

classes= [onesub,sehi,sangoun,sumi,gansu]
temp= []
for i in classes:
    adjusted= adjustScore(i)
    temp.append(adjusted)
avg= sum(temp)//len(classes)
print(avg)