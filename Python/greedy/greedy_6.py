# 동빈나 취업을 위한 코딩 테스트다.
# timer

h= int(input())

count= 0
sec= 60
for i in range(h+1):
    for j in range(sec):
        for k in range(sec):
            if '3' in str(i) +str(j) + str(k):
                count+= 1

print(count)