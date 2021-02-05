V= int(input())
vote_list= list(str(input()))

A_, B_ = 0,0
for i in vote_list:
    if i == 'A':
        A_+= 1
    elif i == 'B':
        B_+= 1

if A_ > B_:
    print('A')
elif A_ == B_:
    print('Tie')
else:
    print('B')