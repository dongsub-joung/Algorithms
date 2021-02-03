# https://www.zerocho.com/category/Algorithm/post/584ba5c9580277001862f188
# 활동 선택 문제
# C[i,j] = max(C[i,k] + C[k,j] + 1 //동적 프로그래밍
# 문제는 이렇게 하면 모든 C들을 구해야함.
'''activity= [
    # [index, begin, end]
    [1,1,3],
    [2,2,5],
    [3,4,7],
    [4,1,8],
    [5,5,9],
    [6,8,10],
    [7,9,11],
    [8,11,14],
    [9,13,16]]'''

def activitySelection(act:list)->list:
    result=[]
    # 끝나는 시간 순으로 정렬
    # C에서 python으로 변환하는데 이 부분 잘 모르겠음.
    '''
    var sorted = act.sort(function(prev, cur) {
    return prev[2] - cur[2];
    })'''
    lambda prev, cur : (prev[2] - cur[2])
    sorted_list= act.sort(key= lambda prev,cur: prev[2]-cur[2])
    #(prev,cur) => prev[2] -cur[2]

    last= 0
    for element in sorted_list:
        # 조건 만족 시 결과 집합에 추가
        if last < element[1]:
            last= element[2]
            result.append(last)
    
    return {x:y for x,y in enumerate(result)} 


# https://gomguard.tistory.com/119
# 지불해야 하는 값이 362원 일 때 1원 50원 100원 짜리 동전으로 동전의 수가 가장 적게 지불하시오.

#list coins는 각각의 동전 타입 coins[0], coins[1], coins[2]: 1, 50, 100
def min_calc(money:int, coins:list)->list:
    '''
    a= []
    for i in coins:
        #list a는 [남은 잔액, 동전 타입] * conis 값만큼
        a.append([money-i,i])
    '''
    a= [[money-i, i] for i in coins]

    res= a[0]
    #list a의 원소 값 list i
    for i in a:
        if (res[0] > i[0]) and (i[0] > 0):
            res= i
    return res


def init():
    #값 초기화
    coin= [1, 50, 100]
    money= [362,0] # 0?
    dic= {}
    #dictionary{key:0}로 초기화, key는 coin의 원소 값
    for i in coin:
        dic[i]= 0

    while True:
        value= min_calc(money[0], coin)
        if value[0] < 0:
            break
        else:
            dic[value[1]] += 1
    print(dic)
init()