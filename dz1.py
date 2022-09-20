# stroka = 'ABc dbE FRl Ama'

# max_up = 0
# up_count = 0
# c = 0

# for i in stroka: 
#     for j in i:
#         upper_count = 0
#         if j.isupper():
            


# # for i in stroka:
# #     c += 1
# #     for j in i:
# #         if i[j].isupper():
# #             up_count += 1
# #         if up_count >= max_up:
# #             max_up = up_count
# #             up_count = 0

# print(100*(c/max_up))

# cu=0
# cl=0
# col = 0
stroka = 'ABc dbE FRl Ama'
def schet(s):
    count_upper=0
    count_lower=0
    for i in s:
        if i.islower():
            count_lower+=1
        elif i.isupper():
            count_upper+=1
    return count_upper>count_lower

summ = 0
count_need = 0
for i in stroka.split():
    count_need += 1
    if schet(i) == True:
        summ += 1
print(summ/count_need*100,'%')

# 


# stroka = 'ABc dbE FRl Ama'
# def schet(stroka):
#     count_upper=0
#     count_lower=0
#     summ = 0
#     count_need = 0
#     for i in stroka.split():
#         count_need += 1
#         if i.islower():
#             count_lower+=1
#         elif i.isupper():
#             count_upper+=1
#     if count_upper>count_lower:
#         summ+=1
#     print(summ/count_need*100,'%')

# schet(stroka)