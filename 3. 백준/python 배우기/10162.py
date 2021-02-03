count_A = count_B = count_C = 0
sec= 60
btn_A= sec*5
btn_B= sec
btn_C= 10
timer= 0

T= int(input())
count_A= T//btn_A
count_B= (T%btn_A)//btn_B
count_C= ((T%btn_A)%btn_B)//btn_C

erorr= ((T%btn_A)%btn_B)%btn_C
if erorr > 0:
    print(-1)
else:
    print(f'{count_A} {count_B} {count_C}')