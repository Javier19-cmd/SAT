import itertools

def fuerzaBruta(cnf_prueba):

	literales_posibles = []

	for conjuncion in cnf_prueba:
		for disjuncion in conjuncion:
			if disjuncion[0] not in literales_posibles:
				literales_posibles.append(disjuncion[0])

	sequencias_posibles = itertools.product([True,False], repeat=len(literales_posibles))

	for sequencia in sequencias_posibles:

		a = [(literales_posibles[i], sequencia[i]) for i in range(len(literales_posibles))]
		lista = []
		for disjuncion in cnf_prueba:
			lista.append(bool(disjuncion.intersection(a)))
		if False not in lista:
			return True, a

	return False

cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}, {("q", False), ("r", False)}, {("p", True), ("q", False), ("r", False)}, {("p", False), ("q", False), ("r", False)}]

print(fuerzaBruta(cnf))