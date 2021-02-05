# https://has3ong.tistory.com/597
def init():
    T = int(input())
    for _ in range(T):
        K = 0
        Y = 0
        for j in range(9):
            A, B = map(int, input().split(' '))
            Y += A
            K += B

        if Y > K:
            print('Yonsei')
        elif Y < K:
            print('Korea')
        else:
            print('Draw')
init()



#                       내가 만든 것
# for _ in range(T):
#     y_, k_= [],[]
#     for _ in range(9):
#         Y, K= map(int, input().split())
#         y_.append(Y)
#         k_.append(K)
    
#     sumed_y= sum(y_)
#     sumed_k= sum(k_)
#     if sumed_y > sumed_k:
#         print('Yonsei')
#     elif sumed_y == sumed_k:
#         print('Draw')
#     elif sumed_y < sumed_k:
#         print('Korea')