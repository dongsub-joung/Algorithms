def init(a:int, b:int)->int:
    if b%a == 0:
        print('factor')
    elif a%b == 0:
        print('multiple')
    else:
        print('neither')

while True:
    x,y= map(int, input().split())
    if x==0 and y==0:
        break
    init(x,y)