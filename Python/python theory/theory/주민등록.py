# 881120-1068234 주민번호 입력시 생년월일과 
# 숫자부분으로 나누어 출력
# + 성별을 나타내는 숫자를 출력해 보자

def Divide(ID_number):
    return ID_number.split('-')
m_ID_number = "881120-1068234"
divided_value = Divide(m_ID_number)
YY_MM_DD = divided_value[0]
private_number = divided_value[1]
man_or_woman = m_ID_number[7]
#print(man_or_woman) //man_or_woman =1
print(f"생년 월일: {YY_MM_DD}")
print(f"주민번호 뒷번호: {private_number}")
if (man_or_woman == "1"): print("성별: 남")
else: print("성별: 여")