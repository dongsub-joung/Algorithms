def checkLeapYear(year:int)->bool:
    if (year%4 == 0) and (year%100 != 0 or year%400 ==0):
        print(1)
    else: print(0)

year_inputed= int(input())
checkLeapYear(year_inputed)