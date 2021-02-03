#  a = "a:b:c:d" -> a#b#c#d 바꾸기

inputed = "a:b:c:d"
doChange = inputed.replace(':','#')
print(f'{inputed} -> {doChange}')