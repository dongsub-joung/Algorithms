coffee =10
while True:
    money = int(input("돈을 넣어 주세요: "))
    payback = money-300
    more_money = 300-money
    if money == 300:
        print("결재 완료. 커피를 줍니다.")
        coffee -= 1
    elif money >300:
        print(f'거스름돈 {payback}를 주고 커피를 줍니다.')
        coffee -= 1
    elif (1< money <300 ):
        print(f'커피는` 300원이니 추가로 {more_money}를 더 내야합니다.')
        money += int(input(f'{more_money}만큼 지불해야합니다.'))
        if money == 300:
            print("결재 완료. 커피를 줍니다.")
            coffee -= 1
    if coffee == 0:
        print("커피 재고가 없습니다.")
        break