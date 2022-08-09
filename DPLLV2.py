def obtenerLiteral(cnf):
	for clausula in cnf:
		for caracter in clausula:
			return caracter[0]

def DPLL(cnf, assignments={}):
	
	if not cnf:
		return True, assignments
	
	for clausula in cnf:
		if len(clausula) == 0:
			return False, None
	
	literal = obtenerLiteral(cnf)

	nuevo_cnf = []

	for clausula in cnf:
		if(literal,True) not in clausula:
			nuevo_cnf.append(clausula)

	# print(nuevo_cnf)

	nuevo_cnf_2 = []

	for clausula in nuevo_cnf:
		nuevo_cnf_2.append(clausula.difference({(literal,False)}))

	# print(nuevo_cnf_2)

	sat, valores = DPLL(nuevo_cnf_2, {**assignments, **{literal: True}})

	if sat:
		return sat, valores

	nuevo_cnf = []

	for clausula in cnf:
		if(literal,False) not in clausula:
			nuevo_cnf.append(clausula)

	nuevo_cnf_2 = []

	for clausula in nuevo_cnf:
		nuevo_cnf_2.append(clausula.difference({(literal,True)}))

	sat, valores = DPLL(nuevo_cnf_2, {**assignments, **{literal: False}})
	
	if sat:
		return sat, valores

	return False, None


cnf = [{("f", False), ("p", False), ("q", False)}] #Se define la clausula.

print(DPLL(cnf)) #Se imprime el resultado.