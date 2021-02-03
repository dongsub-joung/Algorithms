# https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3

def solution(strings, n):
    #sorted(strings, key = lambda element: element[n]) //내가 만든거
    #return sorted([s for s in strings], key = lambda a:[a[n], strings]) 
    
    return sorted(sorted(strings), key= lambda x: x[n])


# https://programmers.co.kr/learn/courses/30/lessons/12915



'''                                              pesudo-code
                                                
index가 되는 char를 뽑은 list를 정렬시킨 후, 
index = n
array_index = [] w 
for element in array:
    array_index.append(element[index])

def selectSort(int_n, list_array):
    #sorted(정렬할 객체, key= 원소의 int_n 번째 글자 기준 정렬)
    sorted(list_array, key = lambda element: element[int_n])

def solution(list_array, int_n):
    answer = []
    answer = sorted(list_array, key = lambda element: element[int_n])
    return answer

a = ["sun", "bed", "car"]
print(solution(a,1))
'''

'''                                             ver 0.0: lambda

listOfLambdas = [(lambda x: x*x) for i in [1,2,3,4,5]]
for f in listOfLambdas: 
print f()
```

```
                                                ver 0.1: lambda

array=[1,2,3,4,5]
result=[]
for s in array:
    result.append((lambda x: x*x)(s))
print(result)
'''

'''                                             ver 0.2: for

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lambda x: x**2 는 주소값이 반환됨.
#<function <listcomp>.<lambda> at 0x009C42F8>
results = [x**2 for x in my_list]
print(results)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

'''                                             ver 0.3: for_dicttionary   

my_dict = {'Java': 21, 'C': 13, 'C++': 7, 'C#': 4, 'Python': 4, 'PHP': 3, 'Javascript': 2, 'Ruby': 2}
#키와 원소를 바꿔서 저장
your_dict = {v: k for k, v in my_dict.items()}
print(your_dict)
'''

'''                                             ver 0.4: list 안에서 짝수 찾기

list_number= [80,15,348,68,18,516,358,846,586]
list_caluated= []
list_caluated= [x for x in list_number if x%2 == 0]
print(list_caluated)
'''