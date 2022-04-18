from random import randint
from time import sleep

colors = {
  'yellow': '\033[1;33m',
  'blue': '\033[36m',
  'purple': '\033[35m',
  'green': '\033[1;30;42m',
  'red': '\033[1;30;41m',
  'clear': '\033[m'
}

separator = colors['yellow'] + '-=-'*20 + colors['clear']
print(separator)
print('{}I\'ll think of a number between 0 and 5. Try to guess...'.format(colors['blue']))
print(separator)
random_number = randint(0, 5)
guess = int(input('What number did I think of? '))
print('{}PROCESSING...'.format(colors['purple']))
sleep(2)
if (random_number == guess):
  print('{}Congratulations! You won!'.format(colors['green']))
else:
  print('{}Not this time, the number is {}. You lost!'.format(colors['red'], random_number))
