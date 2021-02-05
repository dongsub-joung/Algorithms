# 1차
'''
h, m, s =14, 30, 0
add_s = 3600

s= s+ (add_s%60)
m= m+ (add_s//60)

if s >=60:
    m += 1
    s -= 60

# s를 m으로 환산한 것을 기존 값과 더함
if m >=60:
    h +=1
    m -=60

if h >=24:
    h -= 24

print(h,m,s)'''


#2차

h, m, s = map(int, input().split())
#요리하는데 필요한 시간
add_s = int(input()) 

s +=add_s
m += s//60
h += m//60

s= s%60
m= m%60
h= h%24

print(h,m,s)