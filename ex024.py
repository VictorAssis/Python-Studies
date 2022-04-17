city = input('Enter your city: ').strip().upper()
position = city.find('SANTO')
print('Does the city\'s name begin with "Santo"? {}.'.format('Yes' if position == 0 else 'No'))
