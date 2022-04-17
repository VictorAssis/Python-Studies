from math import hypot

opposite = float(input('Enter the length of the opposite side: '))
adjacent = float(input('Enter the length of the adjacent side: '))
hypotenuse = hypot(opposite, adjacent)
print(f'The hypotenuse length is {hypotenuse}.')
