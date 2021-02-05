def cal(x,y,z)->int:
    if x==y and y==z and x==y:
        return 10000+x*1000
    elif x==y:
        return 1000+x*100
    elif z==y: 
        return 1000+y*100
    elif x==z: 
        return 1000+z*100
    else:
        return max(x,y,z)*100

T= int(input())
x_= []
y_= []
z_= []
reward= 0
list_rewards= []

for _ in range(T):
    x,y,z= map(int, input().split())
    x_.append(x)
    y_.append(y)
    z_.append(z)
for i in range(len(x_)):
    x= x_[i]
    y= y_[i]
    z= z_[i]
    list_rewards.append(cal(x,y,z))
result= max(list_rewards)
print(result)