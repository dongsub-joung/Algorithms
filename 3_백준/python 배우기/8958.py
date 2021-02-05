# https://deokkk9.tistory.com/7
n= int(input())

for _ in range(n):
    Num= input()
    score= 0
    sum_score= 0
    for j in Num:
        if j == 'O':
            score+= 1
        else:
            score= 0
        sum_score+= score
    print(sum_score)


#                       첫번째
#  T= int(input())
# for _ in range(T):
#     strings= list(str(input()))
#     count= 0
#     score= 0
#     for i,j in enumerate(strings):
#         if j == 'O':
#             if strings[i+1] == 'O':
#                 count+= 1
#                 score= count
#             print(count)