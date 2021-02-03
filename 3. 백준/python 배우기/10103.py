n= int(input())

default_score= 100
score= [default_score, default_score]
i,j= 0,1
for _ in range(n):
    a,b= map(int,input().split())
    if a > b:
        score[j]-= a
    elif a == b:
        pass
    else:
        score[i]-= b

for n in score:
    print(n)