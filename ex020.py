from random import randint

students = []
for x in range(0, 4):
  students.append(input('Type a student name: '))
print('Presentation order:')
while len(students) > 0:
  randomIndex = randint(0, len(students) - 1)
  print(f'- {students[randomIndex]}')
  del(students[randomIndex])
