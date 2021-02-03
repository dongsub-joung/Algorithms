N= int(input())
count_list= []
cute, not_cute= 0, 0

for _ in range(N):
    inputed= int(input())
    count_list.append(inputed)

for i in count_list:
    if i == 1:
        cute+= 1
    else:
        not_cute+= 1
    
if cute > not_cute:
    print('Junhee is cute!')
elif cute < not_cute:
    print('Junhee is not cute!')


#                       해답 1
# V= int(input())
# cute= 0
# for _ in range(V):
#     if int(input()) == 1:
#         cute+= 1
# if cute > V//2:
#     print('Junhee is cute!')
# else:
#     print('Junhee is not cute!')