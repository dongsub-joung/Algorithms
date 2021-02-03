def is_full(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                return False
    return True

def solution(n):
    a= [[0 for _ in range(i+1)] for i in range(n)] #2차원 배열
    i,j,n= 0,0,1
    while True:
        
        # down
        while True:
            a[i][j]= n
            n+= 1
            if i+1<len(a) and a[i+1][j] == 0:
                i+= 1
            else:
                j+= 1
                break
        if is_full(a):
            break

        # right
        while True:
            a[i][j]= n
            n+= 1
            if j+1< len(a[i]) and a[i][j+1] ==0:
                j+= 1
            else:
                i-= 1
                j-= 1
                break
        if is_full(a):
            break

        # up
        while True:
            a[i][j]= n
            n+= 1
            if i-1> -1 and j-1>0 and a[i-1][j-1] ==0:
                i-= 1
                j-= 1
            else:
                i+= 1
                break
    
        if is_full(a):
            break

    res= []
    for arr in a:
        for val in arr:
            res.append(val)
    return res