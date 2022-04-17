phrase = input('Enter a phrase: ').strip().upper()
print('The letter "a" appears {} times.'.format(phrase.count('A')))
print('The first position of letter "a" is {}.'.format(phrase.find('A') + 1))
print('The last position of letter "a" is {}.'.format(phrase.rfind('A') + 1))
