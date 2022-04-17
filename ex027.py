name = input('Enter the fullname: ').strip()
name_words = name.split(' ')
print(f'First name: {name_words[0]}')
print(f'Last name: {name_words[len(name_words) - 1]}')
