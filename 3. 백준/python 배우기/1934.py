# https://somjang.tistory.com/entry/BaekJoon-1934%EB%B2%88-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98-Python

def gcd(a, b):
    mod= a%b
    while mod > 0:
        a= b
        b= mod
        mod= a%b
    return b

def lcm(a,b):
    return a*b // gcd(a,b)


T= int(input())
for _ in range(T):
    a, b= input().split()
    a= int(a)
    b= int(b)
    print(lcm(a,b))