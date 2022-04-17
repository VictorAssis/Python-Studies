days = int(input('How many days rented? '))
km = float(input('How many km driven? '))
amount = days * 60 + km * 0.15
print(f'The amount to pay is R$ {amount:.2f}')
