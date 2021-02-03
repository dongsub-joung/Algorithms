#https://dojang.io/mod/page/view.php?id=2261
def printOneStep():
    for i in range(5):
        for j in range(5):
            #세로 방향 변수 i 만큼
            if j <= i:
                #별 줄바꿈을 하지 않음
                print("*", end='')
        #가로 방향의 별을 다 그린 뒤 다음 줄로 넘어감
        print()


def diagonal():
    for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
        for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
            if j == i:                # 세로 방향 변수와 같을 때
                print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
            else:                     # 세로 방향 변수와 다를 때
                print(' ', end='')    # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
        print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
                # (print는 출력 후 기본적으로 다음 줄로 넘어감)


def reverseDiagonal():
    for i in range(5):
        for j in range(5):
            if j < i:
                print(' ', end='')
            else:
                print('*', end='')
        print()


#https://dojang.io/mod/quiz/attempt.php?attempt=1073829&cmid=2264
#https://studywith-s2ovely.tistory.com/21
def printPiramid():
    height = int(input())            # 높이 입력
    blank = height-1                 # 빈칸 = 높이 수-1
 
    for i in range(height):          # 세로 방향
        for j in range(height + i):  # 가로 방향 = *이 밑으로 갈 수록 하나씩 늘어남
            if j < blank:            # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
                print(' ', end = '')
            else:                    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
                print('*', end = '')
        print()                      # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
        blank -= 1                   # 밑으로 갈 수록 공백이 하나씩 줄어듦

