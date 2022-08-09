		
def DPLL(cnf_prueba, assignments={}):
	
	def obtenerLit(cnf):
			for conjunto in cnf:
				for caracter in conjunto:
					return caracter[0]

	if not cnf_prueba:
		return True

	for clausula_individual in cnf_prueba:
		if len(clausula_individual) == 0:
			return False

	nuevo_cnf = []

	for clausula_individual in cnf_prueba:
		if (obtenerLit(cnf = cnf_prueba),True) not in clausula_individual:
			nuevo_cnf.append(clausula_individual)

	nuevo_cnf_2 = []

	for clausula_individual in nuevo_cnf:
		nuevo_cnf_2.append(clausula_individual.difference({(obtenerLit(cnf = cnf_prueba),False)}))


	l = obtenerLit(cnf = cnf_prueba)

	print('OBJETO: ',nuevo_cnf_2, {**assignments, **{l: True}})

	sat, valores = DPLL(nuevo_cnf_2, {**assignments, **{l: True}})

	if sat:
		return sat, valores

	nuevo_cnf = []

	for clausula_individual in cnf_prueba:
		if (obtenerLit(cnf = cnf_prueba),False) not in clausula_individual:
			nuevo_cnf.append(clausula_individual)

	nuevo_cnf_2 = []

	for clausula_individual in nuevo_cnf:
		nuevo_cnf_2.append(clausula_individual.difference({(obtenerLit(cnf = cnf_prueba),True)}))

	sat, valores = DPLL(nuevo_cnf_2, {**assignments, **{l: True}})

	if sat:
		return sat, valores

	return False, None


	pass

cnf = [{("f", False), ("p", False), ("q", False)}]
resultado_operacion = DPLL(cnf_prueba = cnf)
print(resultado_operacion)