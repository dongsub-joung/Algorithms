a= int(input())
b= input()
result= list(reversed([a*int(i) for i in b]))

#1*10*100
index= 1
cal= []
for x in result:
    cal.append(x*index)
    index= index*10

for j in result:
    print(j)
print(sum(cal))