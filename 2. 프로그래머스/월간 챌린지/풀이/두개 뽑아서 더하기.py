# 방법 1
def solution(numbers:list)->list:
    answer= []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))

# 방법 2
from itertools import combinations
def solution_two(numbers:list)->list:
    answer= []
    for select in combinations(range(len(numbers)), 2):
        selected= [x for i,x in enumerate(numbers) if i in list(select)]
        answer.append(sum(selected))
    
    answer= sorted(list(set(answer)))
    
    return answer

# 3차
#  def solution(numbers):
#     answers = []
#     i= 0
#     while i==len(numbers):
#         index_val= numbers.pop(i)
#         for j in numbers:
#             answer= index_val+j
#             answers.append(answer)
#         i+= 1
#     answers= list(set(answers))
#     return answers
# arr= [2,1,3,4,1]
# result= solution(arr)
# print(result)

# 2차
# while i >= len(numbers):
#     plus= numbers[i]+numbers[j]
#     answer.append(plus)
#     i,j= 0,1

# 1차
# for i,_ in enumerate(numbers):
#     numbers[i+1:]