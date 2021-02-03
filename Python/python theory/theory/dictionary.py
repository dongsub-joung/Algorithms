# https://dojang.io/mod/quiz/attempt.php?attempt=1073131&cmid=2217#
m_key= input().split()
m_value= input().split()

m_value= list(map(float, m_value))
result= dict(zip(m_key,m_value))
print(result)