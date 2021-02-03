# 동빈나 취업을 위한 코딩 테스트다.
# 숫자카드게임

# 2중 반복문 구조를 이용
n, m= map(int, input().split())
result= 0

for i in range(n):
    data= list(map(input().split()))
    min_value= 1001
    for a in data:
        min_value= min(min_value, a)
    result= max(result, min_value)

print(result)

# min()
n,m= map(int, input().split())
result= 0

for i in range(n):
    data= list(map(int, input().split()))
    min_value= min(data)
    result= max(result, min_value)

print(result)