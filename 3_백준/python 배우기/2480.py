# https://coding-sj.tistory.com/11

a,b,c= map(int, input().split())
prize= 0
if a==b==c:
    prize= 10000 + a*1000
    print(prize)
elif a==b:
    prize= 1000 + a*100
    print(prize)
elif b==c:
    prize= 1000 + b*100
    print(prize)
elif a==c:
    prize= 1000 + c*100
    print(prize)
else:
    prize= max(a,b,c)*100
    print(prize)


# // 1차 시도
'''a,b,c= input().split()
a= int(a)
b= int(b)
c= int(c)
dice= [ a,b,c ]
count= {}
prize= 0
for i in dice:            
    try:
        count[i] += 1
    except:
        count[i]= 1

number= []
count_dice_num= []
for x,y in enumerate(count):
    number.append(x)
    count_dice_num.append(y)
if len(count) == 1:
    prize= 10000 + count[0]*1000
elif len(count) == 2:
    prize= 1000 + count[0]*100
else:
    prize= max(dice)*100

print(prize)'''