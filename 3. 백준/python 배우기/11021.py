def numInput():
    a,b= input().split()
    a,b= int(a),int(b)
    return [a+b]

def Add(a,b)->int:
    return a+b

# init
T= int(input())
add= []

for _ in range(T):
    add.append(numInput())

for i,y in enumerate(add):
    print(f'Case #{i+1}:', y[0])