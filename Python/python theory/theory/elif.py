#https://dojang.io/mod/quiz/attempt.php?attempt=1073785&cmid=2238

age = int(input())
balance = 9000    # 교통카드 잔액

if 7<=age<=12:
    balance-= 650
elif 13<=age<=18:
    balance-= 1050
elif 19<=age:
    balance-= 1250
print(balance)