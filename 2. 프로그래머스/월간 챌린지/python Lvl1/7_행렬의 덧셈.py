# https://programmers.co.kr/learn/courses/30/lessons/12950

def sumMatrix(A,B):
    #A행렬의 길이에 대한 range()를 가지는 i
    for i in range(len(A)) :
        #2차 내부 반복 
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A

arr_1 = [[1,2],[2,3]]
arr_2 = [[3,4],[5,6]]
print(sumMatrix(arr_1,arr_2))