# https://programmers.co.kr/learn/courses/30/lessons/42840
#import numpy as np,numpy
import random
from itertools import cycle

''' pesudo-code
// 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열
answers
//1등 반환
top = [] 
//1,2,3,4,5 중 랜덤한 정답
찍는 방식 =  random(1,5)
'''

                                                                #내가 만든 방식
def makeRandomList(array, max_index):
    array.append(random.randrange(1,max_index))

def BruteForce(answers):
    result= []
    tester_o= []
    tester_tw= []
    tester_th= []

    #tester들의 정답찍기
    choice= 6
    try:
        index= 0
        while True:
            makeRandomList(tester_o,choice)
            makeRandomList(tester_tw,choice)
            makeRandomList(tester_th, choice)
            index += 1
            if len(answers) < index: break
    except:
        print('정답찍기 error')
    
    #찍은 정답과 답안 비교
    score_o= 0
    score_tw= 0
    score_th= 0
    for j in range(len(answers)):
        if answers[j] == tester_o[j]:  score_o += 1
        if answers[j] == tester_tw[j]: score_tw += 1
        if answers[j] == tester_th[j]: score_th += 1

    result= [(score_o), (score_tw), (score_th)]
    sorted(result)
    return result[-1]





#                                                               풀이 1
#문제를 잘 못 이해했다....
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score =    [0, 0, 0]
    result =   []

    for idx, answer in enumerate(answers):
        #pattern1의 길이로 idex를 나눈 나머지에 해당하는 값에 들어있는 수가 답과 같다면 
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        # 리터럴 객체 중 가장 큰 값을 리턴: max() 
        if s == max(score):
            result.append(idx+1)

    return result



#                                                               풀이 2
# 감탄 밖에 안나옴 이건 ㅋㅋ
def solutionTwo(answers):
    p = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        ]
    #외부 배열에 대한 길이를 반환, [0]*3
    s = [0] * len(p)
    #ansers 배열의 index와 value값: q, a
    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            '''
            i: 0 v: [1, 2, 3, 4, 5]
            i: 1 v: [2, 1, 2, 3, 2, 4, 2, 5]
            i: 2 v: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
            '''
            #패턴의 max index를 나누는 값으로 쓰고, 나머지를 반환한 index를 가지는 배열 v값과 ansers배열 값 a와 비교
            if a == v[q % len(v)]:
                s[i] += 1
    # i는 0부터 시작해서 +1
    # 배열 s의 index 0,1,2에 대해서 각각의 value들 중 가장 큰 수가 (반복중)v라면 v에 해당한 i에 대해서 i+1을 반환
    return [i + 1 for i, v in enumerate(s) if v == max(s)]



#                                                            풀이 3
#from itertools import cycle

'''
특정 값이 나올 때까찌 반복, 호출 가능한 객체(callable)를 넣어줌
iter(호출가능한 객체, 반복을 끝낼 값)
iter(lambda : random.randint(0,5),2)
iter(lambda obj, sentinel)
'''
def solutionTh(answers):
    giveups =   [
                #cycle()은 반복 가능한 요소가 모두 소모될때까지 무한 반복하면서 사본을 리턴함.
                cycle([1,2,3,4,5]), #1,2,3,4,5,1,2,3,4,5...
                cycle([2,1,2,3,2,4,2,5]),
                cycle([3,3,1,1,2,2,4,4,5,5]),
                ]
    scores =    [0, 0, 0]
    for num in answers:
        for i in range(3):
            #다음 리터럴 객체 반환
            if next(giveups[i]) == num:
                scores[i] += 1

    highest = max(scores)
    return [i + 1 for i, v in enumerate(scores) if v == highest]