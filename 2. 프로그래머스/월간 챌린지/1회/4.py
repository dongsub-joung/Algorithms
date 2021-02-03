a= [ 
    [0,1,0],
    [1,1,1],
    [1,1,0],
    [0,1,1]
    ]
#전체 열에서 1의 개수가 동일할 경우의 수

def solution(a:list)->int:
    answer = -1
    colums_info= []

    # 조건1. a의 i번째 열과 b의 i번째 열에 들어 있는 1의 개수가 같습니다.
    count= 0
    #a의 i번째 열들의 1의 개수 구하기
    for _ in range(len(a[0])):
        colum_one= [i[count] for i in a].count(1)
        colums_info.append(colum_one)
        count +=1

    # 조건2. b의 각 행에 들어 있는 1의 개수가 짝수입니다. (0도 짝수입니다.)
    b.count(1) % 2
        
    b= [0*len(a)][0*len(a[0])]

    #배열 b를 초기화
    for _,j in enumerate(b):
        for x in j:
            j[x]= 0
            
#경우의 수 구하기
#n*(n-1).... a번
    for numOfCase in colum_one:
        
    
    return answer