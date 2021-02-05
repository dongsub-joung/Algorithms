def cal(fir:int, oper:str, sec:int):
    if oper == '+':
        return fir+sec
    elif oper == '*':
        return fir*sec

first= int(input())
operater= input()
second= int(input())
result =cal(first, operater, second)
print(result)