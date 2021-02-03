import math

num= int(input())

#분해가 전부 될때까지 루프
while num != 1:
    for i in range(2, num+1): #마지막은 안돌리니 +1
        #나눠지면 출력
        #다음을 위해 해당 수로 num을 나눠줌
        if(num % i ==0):
            print(i)
            num= num//i
            break