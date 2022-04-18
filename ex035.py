lines = []
for x in range(0, 3):
  lines.append(float(input('Enter the length of a line: ')))

if lines[0] + lines[1] > lines[2] and lines[0] + lines[2] > lines[1] and lines[1] + lines[2] > lines[0]:
  print('These lines can form a triangle.')
else:
  print('These lines can\'t form a triangle.')
