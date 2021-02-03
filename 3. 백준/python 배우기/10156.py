K, N, M= map(int, input().split())
answer= (K*N)-M
if answer > 0:
    print(answer)
else:
    print(0)


'''price= K*N
remain_M= M-price
if remain_M < 0:
    remain_M= remain_M*-1
print(remain_M)'''