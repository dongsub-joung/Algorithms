a=0
while a<10:
    a+=1
    #a가 짝수일 경우, 조건문으로 다시 돌아감.
    if a%2 == 0:
        continue
    print(a)