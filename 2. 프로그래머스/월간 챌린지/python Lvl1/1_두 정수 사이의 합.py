# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    a_to_b = {}
    answer = 0

    if(a>b): a,b = b,a

    if (a!=b):
        #a에서 b 사이의 정수들을 리스트로 만듬, reango는 마지막 정수를 추가해줘야함.
        a_to_b = list(range(a,b+1))
        #모두 더함
        answer = sum(a_to_b)
        return answer
    elif(a==b):
        answer = a
        return answer