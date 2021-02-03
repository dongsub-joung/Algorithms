# 동빈나 취업을 위한 코딩 테스트다.
# 거스름돈
                                                # 거스름 돈
n= 1260
count= 0

coin_types= [500,100,50,10]

for coin in coin_types:
    count+= n // coin
    n%= coin

print(count)