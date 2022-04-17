name = input('Enter your full name: ').strip()
print(f'- Uppercase: {name.upper()}')
print(f'- Lowercase: {name.lower()}')
name_without_spaces = name.replace(' ', '')
print(f'- Number of letters (no spaces): {len(name_without_spaces)}')
first_name = name.split(' ')[0]
print(f'- Number of letters of first name: {len(first_name)}')
