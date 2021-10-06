# def proverka(text):
# 	if text == text.capitalize():
# 		return True
# 	return False

# text = "Aaaaa"

# print(proverka(text))
# print("")


# def proverka_2(text):
# 	mass = text.split()
# 	if mass[0].capitalize() == mass[0]:
# 		return True
# 	return False






# inic = "Хошев Дмитрий Анатольевич"

# def inicials(text):
# 	mass = text.split()
# 	text = mass[0].capitalize() + " " + mass[1][0] + ". " + mass[2][0] + "."
# 	return text
# print(inicials(inic))
# print("")




# mass_of_inic = ["Хошев Дмитрий Анатольевич", "Иванов Иван Иванович"]

# for i in range (len(mass_of_inic)):
# 	print(inicials(mass_of_inic[i]))
# print("")



# #vvod = input()
# spisok_imen = list()

# while True:
# 	vvod = input()
# 	if vvod == 'q':
# 		break
# 	# print('vvod', vvod)
# 	if proverka_2(vvod) == True:
# 		# print('prov 2 true')
# 		# print(inicials(vvod))
# 		spisok_imen.append(inicials(vvod))
# print(*spisok_imen)

# #print(proverka_2(vvod))


import random


def gen_names(names, second_names, sur_names, num):
    i = 0
    while i < num:
        yield random.choice(names) + " " + random.choice(second_names) + " " + random.choice(sur_names)
        i += 1


for i in gen_names(["Иван", "Фёдр", "Пётр", "Григорий", "Александр"], ["Цыпочкин", "Вертухаев", "Нагиев", "Чёрный", "Мирный"], ["Алексеев", "Дмитриев", "Анатольевич", "Евгеньевич", "Ахмедов"], 10):
    print(i)