# https://programmers.co.kr/learn/courses/30/lessons/12903

                                            # ver 0.1 made me
def solution(s):
    answer = ''
    div = int(len(s)/2)
    
    if len(s)%2 == 0:
        answer = s[div-1]+ s[div]
    else:
        answer = s[div]
    return answer

s = "vczxc"
#print(solution(s))


def string_middle(str):
    #str[begin : end]
    return str[((len(str)-1)//2) : (len(str)//2) +1]
    #2:3  2:4 23 0123456
print(s[2:3])