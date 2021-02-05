# https://pacific-ocean.tistory.com/131

x_list= []
y_list= []
for _ in range(3):
    x,y= map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i])==1:
        x_another= x_list[i]
    if y_list.count(y_list[i])==1:
        y_another= y_list[i]

print(x_another,y_another)