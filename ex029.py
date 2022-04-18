speed = int(input('What is the car\'s speed (km/h)? '))
if speed > 80:
  amount = (speed - 80) * 7
  print(f'You have exceeded the 80km/h limit. The fine is R$ {amount:.2f}.')
print('Have a nice day! Drive safely.')
