#https://dojang.io/mod/quiz/review.php?attempt=1073791&cmid=2246

''' 구구단 출력!
number= int(input())
for i in list(range(1,10)):
    print(f'{number} * {i} ={number*i}')
'''

# https://dojang.io/mod/quiz/review.php?attempt=1073809&cmid=2252

'''
account= int(input())
while account > 0:
    account -=1350
    if account < 0:
        break
    print(account)
'''

start, stop = map(int, input().split())
i = start
 
while True:
    if i%10!=3:
        continue
    if i > stop:
        break
    
    print(i, end=' ')
    i += 1
