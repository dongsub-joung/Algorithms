# https://claude-u.tistory.com/239
T= int(input())

for _ in range(T):
    N= int(input())
    alcohol= []

    for _ in range(N):
        S, L= map(str, input().split())
        alcohol.append([S, int(L)])

    alcohol= sorted(alcohol, key= lambda x:x[1])    # int로 정렬
    result= alcohol[-1][0]
    print(result)

#                   1차
# T= int(input())
# ls= []
# X = L= 0
# S= ""

# for _ in range(T):
#     X= int(input())
#     s, l= input().split()
#     S, L= str(s), int(l)
#     ls.append(L)

# result= max(ls)
# for x,y in enumerate(ls):
#     if result == y:
#         print(x)