salary = float(input('Enter the employee salary: R$ '))
increase = 0.1 * salary if salary > 1250 else 0.15 * salary
print(f'The increase is R$ {increase}.')
print(f'The new salary is R$ {increase + salary:.2f}.')
