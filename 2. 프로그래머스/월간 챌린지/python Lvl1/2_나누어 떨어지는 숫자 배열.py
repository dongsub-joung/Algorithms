
#https://programmers.co.kr/learn/courses/30/lessons/12910
import random

#                                                                               내가 만들었지만 양식에는 맞지 않는것.
#divisor 이용 전 기본 배열을 받음, 배열 set()
def createArr(arr):
    #만약 arr가 비어있다면 1~1000 사이의 자연수를 첫 원소로 추가
    if not arr:
        default_elemente= random.randrange(1,1000)
        arr.append(default_elemente)
        set(arr)
    else:
        #중복 제거, 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
        return set(arr)

#divisor 생성자, 초기화
def createDivisor(number):
    if (number == 0):
        number = random.randrange(1,9)
    return number
    
#divisor를 이용한 array 생성
def createDividedArray(test_set, divisor):
    arr = test_set
    list(arr)
    result_list = []
    for element in arr:
        dived = (element % divisor)
        if dived == 0:
            result_list.append(element)
        else:
            continue
    return result_list


'''
    실행
'''
global m_arr_set
global m_divisor
global m_result

test = [5, 9, 7, 10]
m_arr_set = createArr(test)
m_divisor = createDivisor(5)
m_result = createDividedArray(m_arr_set, m_divisor)
m_result.sort()

if not m_result:
    m_result.append(-1)
    print(m_result)
else:
    print(m_result)

'''#pesudo code
#arr
arr는 최소 1개의 원소를 가짐
default_elemente= rando.randrange()
원소의 중복 x
set()

#divisor
자연수
divisor = rando.randrange(1,9)

dived = arr[i] / divisor
if dived == 0:
    list.append(dived)
    return list.sort()
else:
    return list.append(-1)
'''


#                                                                           양식에 맞춘 것 ver 0.1
def solution(arr, divisor):
    #arry은 자연수 배열. divisor는 자연수 1개
    # 1.divisor로 나누어 떨어지는 수를 배열에 추가
    # 2. 오름차순 정렬
    answer = []

    for element in arr:
        if (element%divisor==0):
            #상위의 index의 값과 비교하면서 더 이상 element값이 작지 않는 index를 찾아서 그 사이에 element를 추가
            answer.append(element)
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer

# 해답 1

2
def solution_two(arr, divisor): 
    #[]=list()
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
