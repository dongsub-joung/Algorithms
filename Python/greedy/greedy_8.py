# 동빈나 취업을 위한 코딩 테스트다.

n, m= map(int, input().split())

d= [[0]* m for _ in range(n)]
x, y, derection= map(int, input().split())
d[x][y]= 1 

# 전체 맵 정보를 입력받기
array= []
for i in range(n):
    array.append(list(map(int, input().split())))

dx= [ -1,0,1,0 ]
dy= [ 0,1,0,-1 ]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction= 3

count= 1
turn_time= 0
while True:
    turn_left()
    nx= x + dx[derection]
    ny= y + dy[derection]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x= nx
        y= ny
        count+= 1
        turn_time= 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx= n - dx[direction]
        ny= y - dy[direction]
        if array[nx][ny] == 0:
            x= nx
            y= ny
        else:
            break
        turn_time= 0

print(count)