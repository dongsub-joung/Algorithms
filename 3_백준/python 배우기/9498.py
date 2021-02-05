''' 1차
def test()->str:
    score= int(input())
    if score>=90 and score<=100:
        print('A')
    elif score>=80 and score<89:
        print('B')
    elif score>=70 and score<79:
        print('C')
    elif score>=60 and score<69:
        print('D')        
    elif score<60 and score>=0:
        print('F')
    else:
        test()
'''        

def test()->str:
    score= int(input())
    if score>=90:
        print('A')
    elif score>=80:
        print('B')
    elif score>=70:
        print('C')
    elif score>=60:
        print('D')        
    else:
        print('F')
test()