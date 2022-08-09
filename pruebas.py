import itertools

# lista = [True,False]

# for i in list(itertools.product(lista, repeat=3)):
# 	print(i)

# somelists = [
#    [1, 2, 3],
#    ['a', 'b'],
#    [4, 5]
# ]

# cart_prod = [(a,b,c) for a in somelists[0] for b in somelists[1] for c in somelists[2]]

# print(cart_prod)


# matrix = [[j for j in range(3)] for i in range(3)]

names = ['Mukesh', 'Roni', 'Chari','hola']
ages = [24, 50, 18,112]
 
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

for i in range(len(names)):
	print(i, names[i], ages[i])

prueba = set([(names[i],ages[i]) for i in range(len(names))])
for i in prueba:
	print(i)





# stocks = ['reliance', 'infosys', 'tcs','lsd']
# prices = [2175, 1127, 2750,112]
 
# new_dict = {stocks: prices for stocks,
#             prices in zip(stocks, prices)}
# print(new_dict)