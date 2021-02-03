a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# 30 in a
# True

# 100 not in a
# True

#튜플, range, 문자열은 읽기 전용입니다.

# 시퀀스객체[begin: end]
# 끝 인덱스는 실제로 가져오려는 인덱스보다 1을 더 크게 지정해야 합니다.
# len()을 이용해서 구한 max index는 그대로 사용하면 됨.
# 마지막 index를 포함하지 않으니 1을 더할 필요가 없음

# a[5:1:-1]
# 끝 인덱스는 가져오려는 범위에 포함되지 않습니다.

# [] == __getitem__

# https://dojang.io/mod/quiz/attempt.php?attempt=1072679&cmid=2212
def deleteLateFiveElement():
    x = input().split()
    for i in range(1,6):
        x.pop()
    return (tuple(x))

# https://dojang.io/mod/quiz/attempt.php?attempt=1072806&cmid=2473
A= list(input())
B= list(input())
string= ""
for i in (A[1::2] + B[0::2]):
    string += i
print(string)