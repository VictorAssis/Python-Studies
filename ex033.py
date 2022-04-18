smaller = None
bigger = None
for x in range(0, 3):
  number = float(input('Type a number: '))
  if not smaller:
    smaller = number
    bigger = number
  else:
    if number < smaller:
      smaller = number
    if number > bigger:
      bigger = number
print(f'Smaller: {smaller}\nBigger: {bigger}')
