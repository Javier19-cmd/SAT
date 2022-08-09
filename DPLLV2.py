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

	nuevo_cnf_2 = []

	for clausula in nuevo_cnf:
		nuevo_cnf_2.append(clausula.difference({(literal,False)}))

	sat, valores = DPLL(nuevo_cnf_2, {**assignments, **{literal: True}})

	if sat:
		return sat, valores

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
	

	if sat:
		return sat, valores

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