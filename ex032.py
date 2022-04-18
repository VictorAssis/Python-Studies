from datetime import date

year = int(input('Type a year (enter 0 for the current year): '))
if year == 0:
  year = date.today().year
is_divisible_4 = year % 4 == 0
is_divisible_100 = year % 100 == 0
is_divisible_400 = year % 400 == 0
if is_divisible_4 and not is_divisible_100 or is_divisible_400:
  print(f'The year {year} is a leap year.')
else:
  print(f'The year {year} is a not leap year.')
