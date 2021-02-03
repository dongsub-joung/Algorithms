# https://programmers.co.kr/learn/courses/30/lessons/64061

'''
for i in range(len(board)):            # 세로 크기
    for j in range(len(board[i])):     # 가로 크기
        print(board[i][j], end=' ')
    print()

def calulateColum(board):
    return len(board[0:])

def saveEachColum(colum):
    list_result = []
    #low 반복
    for i in range(len(board)):
        #입력받은 colum의 low들을 반복해서 받아옴
        value = board[i][colum]
        #list
        list_result.append(value)
    list_result = list(reversed(list_result))
    return list_result

def SavepopValue(list_colum):
    #colum_index = list(range(0,max_colum))
    poped = 0
    while poped == 0:
        poped = list_colum.pop()
    return poped

    init

g_max_colum = calulateColum(board)
g_list_zero_colum = saveEachColum(0)
m_poped = SavepopValue(g_list_zero_colum)
'''

def solution(board, moves):
    stacklist = []
    answer = 0

    #moves의 원소를 i에 대입
    for i in moves:
        #board의 밖 행렬의 수를 range,j에 대입
        for j in range(len(board)):
            #행렬의 j번째 행렬의 i-1번째 원소가 0이 아니면
            if board[j][i-1] != 0:
                #board[j][i-1]의 원소를 stacklist에 추가
                stacklist.append(board[j][i-1])
                #추가한 값은 0으로 초기화
                board[j][i-1] = 0

                #만약 stacklist의 길이가 1보다 크면
                if len(stacklist) > 1:
                    #그리고 stacklist의 -1번째 원소와 -2번째 원소가 같으면
                    if stacklist[-1] == stacklist[-2]:
                        #-1번째 원소를 pop() //원소를 끌어내고 삭제 *2
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        #없어진 원소는 2개
                        answer += 2     
                #for 반복문 탈출
                break

    return answer

board = [
        [0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]
        ]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))