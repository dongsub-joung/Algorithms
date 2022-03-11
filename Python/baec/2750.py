# Insert
N= int(input())
M= []

for i in range(N):
    M.append(int(input()))

for i in range(1,len(M)):
    while (i>0) & (M[i] < M[i-1]):
        M[i], M[i-1]= M[i-1], M[i]
        i-= 1

for n in M:
    print(n)


# Bubble
N= int(input())
M= []

for i in range(N):
    M.append(int(input()))

for i in range(Len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i], M[j]= M[j], M[i]

for n in M:
    print(n)