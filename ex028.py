from random import randint
from time import sleep

random_number = randint(0, 5)
guess = int(input('Try to guess. What number between 0 and 5 did I think of? '))
print('PROCESSING...')
sleep(2)
if (random_number == guess):
  print('Congratulations! You won!')
else:
  print(f'Not this time, the number is {random_number}. You lost!')
