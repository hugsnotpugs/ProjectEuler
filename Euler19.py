'''
1/1/1900 is a Monday
4, 6, 9, 11 have 30 days
1, 3, 5, 7, 8, 10, 12 have 31
2 has either 28 or 29 (every 4 years)

How many sundays are on the first of a month during the 20th century?
'''

def check_sunday(weekday):
	if weekday == 7:
		return True
	else:
		return False

def change_time(year, month, day, weekday):
	thirties = (4, 6, 9, 11)
	thirty_ones = (1, 3, 5, 7, 8, 10, 12)
	febs = (2)

	# Change day and weekday
	day += 1
	weekday += 1
	if weekday > 7:
		weekday = 1

	# Change month
	if month in thirties and day > 30:
		month += 1
		day = 1
	elif month in thirty_ones and day > 31:
		month += 1
		day = 1
	elif month == 2 and year%4 == 0 and year != 1900 and day > 29:
		month += 1
		day = 1
	elif month == 2 and (year%4 != 0 or year == 1900) and day > 28:
		month += 1
		day = 1

	# Change year
	if month > 12:
		year += 1
		month = 1

	return year, month, day, weekday

# Run calculations
year = 1900
month = 1
day = 1
weekday = 1
num_sundays = 0

while year < 2001:
	if check_sunday(weekday) and year >= 1901 and day == 1:
		num_sundays += 1
	year, month, day, weekday = change_time(year, month, day, weekday)

print num_sundays


