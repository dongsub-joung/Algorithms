def cal(A,B)->int:
    if A<B:
        A,B= B,A
    print(A+B)
    print(A-B)
    print(A*B)
    print(int(A/B))
    print(int(A%B))

A, B= input().split()
A= int(A)
B= int(B)
cal(A,B)