requested_toppings = []
for requested in range(1,4):
    requested = input('Escolha os indredientes:')
    requested_toppings.append(requested)
if 'mushrooms' in requested_toppings:
    print('OHHHHH YES MUSHROOMS!!')
else:
    print('Go!')

