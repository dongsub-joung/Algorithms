#소수 판별하기

def is_prime(n: int)-> bool:
    # 1은 소수가 아님
    if n<2:
        return False
    # 2,3은 무조건 소수임
    if n in (2,3):
        return True
    # 2 나 3으로 나누어지면 소수가 아님
    if (n%2 is 0) or (n%3 is 0):
        return False
    # 9보다 작은 수 중에 위의 조건을 만족시키는 수는 소수임
    if n<9:
        return True
    # K는 홀수인 5, 7, 11, 15,...의 패턴.
    # I는 n의 제곱근을 검사하기 위한 것. (루트 n)
    K, I= 5, n**0.5
    while K <= I:
        # 5 혹은 7로 나누어 떨어지면 소수가 아님
        if n&K is 0 or n&(K+2) is 0:
            return False
        # 다음은 11부터 쭉(3의 배수를 뺀 홀수들을 검사)
        K += 6
    return True


#에라토스테네스의 체
#2부터 시작하는 연속된 자연수를 미리 써 두고, 
#처음 나타나는 수의 배수들을 모두 지우는 식으로 나아가서
#소수만 남기는 방식으로 구한다.
#이 방식은 미리 소수가 나타날 범위를 한정해야 한다는 단점이 있다

def primesUpTo(n: int)-> [int]:
    # 1,2 제외 + 3 소수 *n-1개
    seive= [False, False] + [True] * (n-1)
    #key,value
    for i,e in enumerate(seive):
        #value에 대해서
        if e:
            #index *2
            k= i*2
            #index에 2를 곱한 것(2의 배수, k)보다 n이 커질 때까지
            while k <= n:
                #k번째 seive의 값은 소수가 아님
                seive[k]= False
                #다음 2의 배수
                k += i
    # y가 참이면 x값의 list를 리턴
    return [x for x,y in enumerate(seive) if y]


# 파이썬의 슬라이스 문법을 이용한 치환
# 특정 범위와 스텝을 통해 구간을 정할 수 있다. 
# 이를 이용해서 리스트 내의 불연속적인 부분집합을 매우 빠르게 치환할 수 있다.

def primesUpToGood(n:int)->[int]:
    seive= [False, False] +[True]*(n-1)
    for k in range(2, int(n** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k]= [False]*((n-1) // k)
    return [x for x in  range(n+1) if seive[x]]

