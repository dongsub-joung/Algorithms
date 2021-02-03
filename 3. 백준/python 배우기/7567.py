dish= input()
dish= list(dish)

high= 10

for i in range(1, len(dish)):
    if dish[i-1] != dish[i]:
        high+= 10
    else:
        high+= 5

print(high)


# 1차
#  inputed= input()
# count= []
# high= 0

# for i in inputed:
#     count.append(i)
# count.pop(0)
# high+= 10

# for index, char in enumerate(count):
#     if char == '(':
#         high+= 5
#     elif char == ')':
#         if index/2 == 0:  
#             high= len(count)*10

# print(high)