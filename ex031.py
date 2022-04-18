distance = int(input('What is the travel distance in km? '))
price_km = 0.5 if distance <= 200 else 0.45
print(f'The price is {(price_km * distance):.2f}.')
