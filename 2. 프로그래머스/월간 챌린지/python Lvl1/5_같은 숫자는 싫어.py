# https://programmers.co.kr/learn/courses/30/lessons/12906

''' Pesudo
#enumerate: (index number, element)형식으로 리턴
#get() 특정 키에 대한 값을 리턴, default= None
#array[i]의 값 v의 값이 array[i+1]의 v값과 같으면 
0,1
1,1
2,3
3,3
4,0
5,1
6,1
'''

def no_continuous(list_inputed):
    result_list = []

    for list_value in list_inputed:
        #(result_list에 존재하는 값 == 현재 index의 값)의 경우 continue
        if result_list[-1:] == [list_value]: 
            continue
        #두 element가 다르면 result_list에 추가
        result_list.append(list_value)
    return result_list


'''
    init
'''
result = no_continuous( "1133011" )
print(result)