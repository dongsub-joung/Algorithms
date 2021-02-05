word= list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)

#                          내가 만든 것 심지어 틀림 ㅋㅋ..
#  def pellindrom(strings:str)->int:
#     string= strings
#     pivot= 0
    
#     if len(string)%2 == 0:
#         pivot= len(string)//2
#         first= sorted([ i for i in string[:pivot]])
#         second= reversed([ j for j in string[pivot:]])
#         return first == second
#     else:
#         pivot= len(string)//2
#         first= sorted([ i for i in string[:pivot]])
#         second= reversed([ j for j in string[pivot+1:]])
#         return (first == second)

# inputed= str(input())
# result= pellindrom(inputed)
# print(int(result))