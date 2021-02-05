a, b= input().split()
number_all= int(a)
averag= int(b)

# 평균= 저작권 개수 / 수록곡 개수
# 저작권 개수= 평균*수록곡 개수

copyright_number= number_all*(averag-1)+1
print(copyright_number)