def stringMulti(num:int,string:str)->str:
    temp= []
    for i in string:
        temp.append(i*num)
    return ''.join(temp)
    
T= int(input())
for t in range(T):
    r,S= input().split()
    R= int(r)
    print(stringMulti(R,S))



''' 1차
def stringMulti(num:int,string:str)->str:
    list= string.split()
    temp= []
    P= ""
    for i in list:
        temp.append(i*num)
    for j in temp:
        P= P+j
    return P
'''

''' 테스트
string= "asdfsv"
num= 2
for i in string:
    print(i*num)
'''