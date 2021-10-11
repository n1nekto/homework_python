# something = input()

# def palindrome(something):
# 	return something == something[::-1]

# print(palindrome(something))

# num = input()

# def num_six(num):
# 	return num*6

# print(num_six(num))

# num = input()
# n = int(input())
# def num_six(num, n):
# 	return num*n

# print(num_six(num, n))


day, month, year = map(int, input().split())

# def help(f):
# 	'''
# 			  --information--
# That function is founding is that date was or no
#    All you need is just input: day month yer
# 			 Something like this
# 	'''


def proverka_dat(day, month, year):
	'''
			  --information--
That function is founding is that date was or no
   All you need is just input: day month yer
			 Something like this
	'''
	if month <= 12 and year <= 2021 and day <= 31 and (day and month or year) >= 0:
		if (year%4 == 0 and month == 2 and day > 29) or (year%4 != 0 and month == 2 and day > 28):
			return False
		elif (month == 4 and day > 30) or (month == 6 and day > 30) or (month == 8 and day > 30) or (month == 11 and day > 30):
			return False
		# elif day or month or year < 0:
		# 	return False
		return True	
	else:
		return False

if proverka_dat(day, month, year) == True:
	print('Дата существует.')
else:
	print('Такой даты нет.')
