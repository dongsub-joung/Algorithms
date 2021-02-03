n,m= input().split()
n,m= int(n),int(m)
print(n*m-1)

# 한쪽으로 M-1번 쪼개야하고
# 다른 한쪽은 (N-1)을 각각 M번 쪼개야함.
# (M-1) + M(N-1) = M-1+MN-M
# =MN-1