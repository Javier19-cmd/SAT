#Metodo utulizado para obtener el literal a evaluar
def obtenerLiteral(cnf):
	for clausula in cnf:
		for caracter in clausula:
			return caracter[0]

def DPLL(cnf, assignments={}):
	# Si el length de la clausula es 0 se retorna True junto con las asignaciones resultantes.
	if not cnf:
		return True, assignments
	
	# Si el size de alguna clausula es 0 se retorna False.
	for clausula in cnf:
		if len(clausula) == 0:
			return False, None
	
	# Se obtiene el primer literal que se encuentre en la clausula.
	literal = obtenerLiteral(cnf)

	# Se eliminan todas las clausulas que contengan el literal l en el cnf.
	nuevo_cnf = []

	for clausula in cnf:
		if(literal,True) not in clausula:
			nuevo_cnf.append(clausula)

	# Se eliminan las ocurriencias del literal l en las clausulas para el cnf y obtener el nuevo cnf' == cnf_2.
	nuevo_cnf_2 = []

	for clausula in nuevo_cnf:
		nuevo_cnf_2.append(clausula.difference({(literal,False)}))

	# Al resultado de cnf' se le aplica el algoritmo con una I' la cual se compone de I U l:True.
	sat, valores = DPLL(nuevo_cnf_2, {**assignments, **{literal: True}})

	# Si el resultado de SAT es True se retornan los valores.
	if sat:
		return sat, valores

	# En el caso de no acceder al previo If, se realiza la misma prueba en el complemento del conjunto:
	nuevo_cnf = []

	for clausula in cnf:
		if(literal,False) not in clausula:
			nuevo_cnf.append(clausula)

	nuevo_cnf_2 = []

	print('Clausula 1: ',{**assignments, **{literal: True}})

	for clausula in nuevo_cnf:
		nuevo_cnf_2.append(clausula.difference({(literal,True)}))

	print('Clausula 2: ',{**assignments, **{literal: False}})

	sat, valores = DPLL(nuevo_cnf_2, {**assignments, **{literal: False}})
	
	# Si el complemento del conjunto es verdadero se retorna True junto a sus valores.
	if sat:
		return sat, valores

	# Si no se retorna False.
	return False, None


cnf = [{("f", False), ("p", False), ("q", False)}] #Se define la clausula.
print(DPLL(cnf))
cnf = [{('a', False), ('b', False)}, {('a', False), ('b', False)}]
print(DPLL(cnf))
cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}]
print(DPLL(cnf))
cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}, {("q", False), ("r", False)}]
print(DPLL(cnf))
cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}, {("q", False), ("r", False)}, {("p", True), ("q", False), ("r", False)}]
print(DPLL(cnf))
cnf = [{("p", True)}, {("p", False)}]
print(DPLL(cnf))