#https://programmers.co.kr/learn/courses/30/lessons/12933

def intToString(int_n):
    string_n = str(int_n)
    result_list = []

    for value in string_n:
        result_list.append(value)
    return sorted(result_list, reverse=True) 

def stringToInt(string_list):
    suming = ''
    for value in string_list:
        suming += value
    return suming

inputed_value = intToString(118372)
result = stringToInt(inputed_value)
print(result)