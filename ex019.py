from random import choice

students = []
for x in range(0, 4):
  students.append(input('Type a student name: '))
sorted = choice(students)
print(f'{sorted} must erase the board.')
