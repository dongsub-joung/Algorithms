def solution(numbers:list)->list:
    answer = []

    for j in range(len(numbers)):
        for index, element in enumerate(numbers):
            if j == index:
                pass
            else:
                answer.append(numbers[j] + element)        
    return sorted(list(set(answer)))

    ''' #i를 배열 전체와 비교, 덧셈
   for index, element in enumerate(numbers):'''