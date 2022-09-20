# import calendar
# day, month, year = map(int, input().split())

# def proverka_dat(day, month, year):
# 	if month <= 9 and year <= 2022 and day <= 31 and (day and month or year) >= 0:
# 		if (year%4 == 0 and month == 2 and day > 29) or (year%4 != 0 and month == 2 and day > 28):
# 			return False
#         # elif (year%100)
# 		elif (month == 4 and day > 30) or (month == 6 and day > 30) or (month == 8 and day > 30) or (month == 11 and day > 30):
# 			return False
# 		return True	
# 	else:
# 		return False

# if proverka_dat(day, month, year) == True:
# 	print('Дата существует.')
# else:
# 	print('Такой даты нет.')


# day, month, year = map(int, input().split())
# def isl(year):
# 	if year%4 == 0 and year%400 == 0:
# 		return True
# 	elif year%4 == 0 and year% 400 == 0 and year% 100 == 0:
# 		return False
# 	return False

# def is_date_real():
# 	try:
# 		day, month, year = map(int, input().split())
# 	except Exception:
# 		print('Input date in format: dd mm yyyy')
# 		return False 
# 	else:
# 		# day_now = 20
# 		# month_now = 9
# 		# year_now = 2022
# 		leap_february = (isl(year) == True and month == 2)
# 		not_leap_february = (isl(year) == False and month)

# 		# if day > (day_now) or month > (month_now) or year > year_now:
# 		# 	flag = False
# 		if day > 31 or month > 12:
# 			flag = False
# 		elif leap_february and day > 29 or not_leap_february and day > 28:
# 			flag = False
# 		elif (month == 4 and day > 30) or (month == 6 and day > 30) or (month == 8 and day > 30) or (month == 11 and day > 30):
# 			flag = False
# 		else:
# 			flag = True
		
# 	return flag
from dz2_module import is_date_real
if is_date_real():
	print('Date is real!')
else:
	print('Fake date!')