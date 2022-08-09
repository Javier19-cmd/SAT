# cnf = [{("f", False), ("p", False), ("q", False)}] 

# if len(cnf) == 0:
# 	print("True")

# if not cnf:
# 	print('True')

# for c in cnf:
#         for literal in c:
#             print(literal[0])

def sumar(*argumentos):
	print(argumentos,'hola')
	return sum(argumentos)

def suma(nu1, nu2, nu3):
	return nu1 + nu2 + nu3

def imprimirUsuario(**usuario):
	print(usuario)
	return True
	

# print(suma(3,4,5))
sumar(3,4,5)

# print(sumar(1,2,3,4,5,8,9,0,9))

print(imprimirUsuario(nombre = "Juan", apellido = "Perez"))