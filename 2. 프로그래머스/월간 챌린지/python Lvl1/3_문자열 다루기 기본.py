#https://programmers.co.kr/learn/courses/30/lessons/12918
import re

def checkDataType(inputed):
    #변수의 클래스 인스턴스를 확인해서 비교, 맞으면 True, 아니면 False: 'isinstance'
    return isinstance(inputed,str)
    
def boolNumber(inputed):
    #string에 숫자가 포함되어 있으면 True, 없으면 False: 'isdigit()'
    return inputed.isdigit()

#init
s = input()
s_length = len(s)

try:
    #'s`의 데이터 타입이 string이라면 
    if checkDataType(s):
        if 0<s_length<9:
            print(boolNumber(s))
        else:
            print('길이 1 이상, 길이 8 이하인 문자열을 입력하시오.')
except:
    print('Error')

'''pesudo
inputed s
def 데이터 형 검사
if string이면 pass
if(0<s.size()<9)
else:
    print('길이 1 이상, 길이 8 이하인 문자열을 입력하시오.')

limit_number = re.compile('0-z9')
limit_number.match(s)
'''

def solution(s):
    #s는 char 1~8
    if (len(s) ==4) or (len(s)==6):
        if s.isdigit() == True:
            return True
        else:
            return False

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)