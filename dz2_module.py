def isl(year):
	if year%4 == 0 and year%400 == 0:
		return True
	elif year%4 == 0 and year% 400 == 0 and year% 100 == 0:
		return False
	return False

def is_date_real():
	try:
		day, month, year = map(int, input().split())
	except Exception:
		print('Input date in format: dd mm yyyy')
		return False 
	else:
		# day_now = 20
		# month_now = 9
		# year_now = 2022
		leap_february = (isl(year) == True and month == 2)
		not_leap_february = (isl(year) == False and month)

		# if day > (day_now) or month > (month_now) or year > year_now:
		# 	flag = False
		if day > 31 or month > 12:
			flag = False
		elif leap_february and day > 29 or not_leap_february and day > 28:
			flag = False
		elif (month == 4 and day > 30) or (month == 6 and day > 30) or (month == 8 and day > 30) or (month == 11 and day > 30):
			flag = False
		else:
			flag = True
		
	return flag
