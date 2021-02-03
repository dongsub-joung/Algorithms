#https://dojang.io/mod/quiz/view.php?id=2234
#내가 짬
'''score= input().split()
for i in score:
    if 100 < int(i) < 0:
        print('잘못된 점수')
    else:
        break
s= sum(score)/len(score)
if s >= 80:
    print('합격')
else:
    print('불합격')'''

korean, english, mathematics, science= map(int, input().split())
condition_kor= 0 <= korean <= 100
condition_eng= 0 <= english <= 100
condition_math= 0 <= mathematics <= 100
condition_science= 0 <= science <= 100

if condition_kor and condition_eng and condition_math and condition_science:
    average= (korean+english+ mathematics+ science) / 4
    if average >= 80:  print('합격')
    else: print('불합격')
else: print('잘못된 점수')