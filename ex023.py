number = input('Enter a number between 0 e 9999: ')
numberSize = len(number)
print(f'- Units: {number[numberSize - 1]}')
if (numberSize > 1):
  print(f'- Tens: {number[numberSize - 2]}')
if (numberSize > 2):
  print(f'- Hundreds: {number[numberSize - 3]}')
if (numberSize > 3):
  print(f'- Thousands: {number[numberSize - 4]}')
