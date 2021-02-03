def solution(info:list, query:list)->list:
    answer = []
    info.split(' ')

    return answer

'''
query의 배열을 str로 쪼갬
쪼갠 배열에서 [::2]를 이용 and 빼고 가져옴
info도 동일하게 쪼깬 list에서 [0]부터 [-1]까지 조건을 비교함.
조건은 4가지로 되어 있어서 4열, N행
# 열마다 리스트를 만들어서 query 정보에 해당하는 조건을 순서대로 검색하면 되지 않을까?
해당 열마다 True *4번이면 해당 query의 index에 +1

'''


info= ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query= ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

query_= [query_value.split(' ') for query_value in query]
query_lists= [i[::2] for i in query_]

info_colums= []
info_lists= [info_value.split(' ') for info_value in info]
for index in range(5):
    info_colums.append([x[index] for x in info_lists])



query_lists[0]
'''for idx, colum_list in enumerate(query_lists):
    for inner_idx, val in enumerate(colum_list):
        if val in info_colums[idx] == False:
            break'''


#print(info_colums)
for index in len(query_lists):
    for inner_idx in query_lists[index]:
print(query_lists[0])


#print(query_lists[0:1:2])