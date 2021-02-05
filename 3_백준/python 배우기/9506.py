# https://home-body.tistory.com/395

while True:
    n = int(input())
    if n == -1:
        break
    arr= [i for i in range(1, (n//2)+1) if not n%i]
    if n == sum(arr):
        print(f'{n} = {" + ".join(map(str, arr))}')
    else:
        print(f'{n} is NOT perfect.')


#                       내가 만든 것
# def func(n:int):
#     start= 1
#     perfect= sorted([i for i in range(start, n) if n%i == 0])
#     if sum(perfect) == n:
#         print(f'{n} = ',end='')
#         for i in perfect:
#             print(f'{i}', end='+')
#     else: 
#         print(f'{n} is NOT perfect.')
# num= 0
# while True:
#     num= int(input())
#     if num == -1:
#         break
#     func(num)