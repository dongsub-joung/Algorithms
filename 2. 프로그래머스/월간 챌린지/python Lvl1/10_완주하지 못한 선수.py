# https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

# 1번째 방법
def solution(participant, completion):
    #여집합 key, 원소= participant list의 원소들 - completion의 원소들 
    answer = collections.Counter(participant) - collections.Counter(completion)
    #key, 한명만이 제외되어서
    return list(answer.keys())[0]


'''
문자열 데이터는 해쉬 함수를 거쳐 숫자로 변경된다. 
변경된 이 값(해시)를 배열의 키로 삼아 밸류를 저장한다. 
데이터를 서칭하는 과정에서 배열을 순차적으로 탐색할 필요없이 해시 함수를 거쳐 생성된 해시 값으로 데이터를 빠르게 찾을 수 있다. 
딕셔너리의 key-value 구조와 유사하다.
'''
#2번째 방법
def solutionTwo(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        #dictionary를 이용, hash()
        #해시(Hash): 인풋 데이터를 고정된 길이의 숫자열로 변환한 결과물 
        dic[hash(part)] = part
        #다음 주소 값(포인터에 바이트 수를 더하는 것과 동일?)
        temp = temp + int(hash(part))

    for com in completion:
        temp = temp - hash(com)

    #최종 배열의 해쉬값
    answer = dic[temp]

    return answer


#                                               ver 0.1
#def stringCheck(name):
#    a_to_z = re.compile('[^a-z]',{name})
#    print(str(a_to_z))
#    return str(a_to_z.search(name))

#def stringCheck_two(name):
    #pattern = re.compile([^a-z])

#result= stringCheck('namu')
#print(result)


'''                                             ver 0.2
import re

m_participant = []
m_completion = []
dict_participant = dict()

#해쉬화: map<string,stirng>
def DicPerson(m_participant, m_completion):
    #만약 참가자의 이름은 1개 이상 20개 이하면
    if (0<m_participant<=20):
        #해당 정규식을 만족하면 객체를 리턴
        if(stringCheck(m_participant)):
            #map<name, participant> 
            dict_participant[m_participant] = m_completion
        else:
            print('이름이 소문자가 아닙니다.')
    else:
        print('글자 수가 1~20의 범위에 벗어납니다.')

#알파벳 소문자, 정규식 객체 이용
def stringCheck(name):
    a_to_z = re.compile('a-z')
    return a_to_z.match(name)
'''