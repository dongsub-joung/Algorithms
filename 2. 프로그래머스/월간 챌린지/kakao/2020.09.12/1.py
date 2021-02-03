'''
길이 3~15
아이디 a-z,0-9, - _ .
. 는 [0] [-1] 사용 x, 연속으로 사용x

'''

import re

def solution(new_id:str)->str:
    answer = ''
    one_two_step= re.sub('[^-_.a-z0-9_]','', new_id.lower())
    th_step= re.sub('[\.]+', '.', one_two_step)
    
    list_th_step= list(th_step)
    fo_step= list_th_step[0].replace('.',"") + list_th_step[1:-1] + list_th_step[-1].replace('.',"")
    
    if fo_step == "":
        fo_step= 'a'
    
    if len(fo_step) >= 16:
        six= fo_step[:16]
        if six[15] == '.':
            sev= six[15].replace('.', '')

    sev_len= len(sev) 
    if sev_len <= 2:
        while sev_len == 3:
            sev += sev[-1]
            answer= sev

    return answer