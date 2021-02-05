def cal(num:int, item:str)->int:
    if(item == '@'):
        return num*3
    elif (item == '%'):
        return num+5
    elif (item == '#'):
        return num-7

T= int(input())             # 테스트케이스의 개수 T
for i in range(T):          # T번 실행
    list= input().split(" ")# 입력받은 값을 공백을 넣어 저장
    num= float(list.pop(0)) # 리스트의 0번째 값을 float형식으로 num에 저장
    for j in list:          # list에 남은것은 연산식 뿐 그것을 실행
        num= cal(num, j)    # list의 연산식을 j로 꺼내서 cal 함수 실행 후 num에 저장
    print("%.2f" % num)     # 소수점 두 자리까지 