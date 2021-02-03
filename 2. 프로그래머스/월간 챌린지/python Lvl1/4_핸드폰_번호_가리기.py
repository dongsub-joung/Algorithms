#https://programmers.co.kr/learn/courses/30/lessons/12948

'''pesudo

inputedNumber()     번호 입력받음
handeler = ^-4:0, * 뒷 4자리부터 -1까지
result
'''

class HideBackNumber:

    def inputedNumber(self):
        print('숫자만 입력하시오.')
        string = input()
        return string

    def checkingString(self,string):
        try:
            if string.isdigit() == False:
                raise Exception()
            else:
                return True
        except:
            print('문자열이 들어가 있습니다.')

    def replaceRange(self, string):
        return string[-4:]

    def remainRange(self, string):
        return string[:-4]

    def changeDividedString(self, remain_string, replace_string):
        len_max_remain = len(remain_string)
        g_remain_range = "*" * len_max_remain
        return g_remain_range + replace_string
        

'''
    init
'''
global g_phone_number
global g_replace_range
global g_remain_range
result= ""
hide_number = HideBackNumber()

#숫자를 string으로 입력받기
g_phone_number = hide_number.inputedNumber()
#입력받은 string에 문자가 존재하는지 필터
b_checked = hide_number.checkingString(g_phone_number)

try:
    if b_checked ==True:
        g_remain_range = hide_number.remainRange(g_phone_number)
        g_replace_range = hide_number.replaceRange(g_phone_number)
        result = hide_number.changeDividedString(g_remain_range, g_replace_range)
        print(result)
except:
    print('Error')


#양식에 맞춘 것.

def solution(phone_number):
    start_range= "*" * len(phone_number[:-4])
    return start_range + phone_number[-4:]