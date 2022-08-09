# Se importa itertools para poder acceder a su funcion de producto cartesiano.
import itertools

def fuerzaBruta(cnf_prueba):
	# Realizamos una lista en la que se almacenan los literales que pueden ocurrir:
	literales_posibles = []
	# Agregamos todos los caracteres dentro del cnf sin que ocurra una repeticion.
	for conjuncion in cnf_prueba:
		for disjuncion in conjuncion:
			if disjuncion[0] not in literales_posibles:
				literales_posibles.append(disjuncion[0])

	# Realizamos un producto cartesiano de los elementos [True, False] para cada literal:
	sequencias_posibles = itertools.product([True,False], repeat=len(literales_posibles))

	# Recorremos todas las posibles secuencias generadas previamente:
	for sequencia in sequencias_posibles:
		# Se adjunta cada literal con su estado de tal manera que se ordenen de la siguiente manera: [('q', True), ('p', True), ('r', True)]
		a = [(literales_posibles[i], sequencia[i]) for i in range(len(literales_posibles))]

		lista = []
		# Se recorre cada disjuncion en el cnf:
		for disjuncion in cnf_prueba:
			# Se agrega a la lista True|False dependiendo si la disjuncion es satisfactoria o no:
			lista.append(bool(disjuncion.intersection(a)))
		# Si todas las disjunciones son satisfactivas, se devuelve True junto al cnf que cumple las condiciones:
		if False not in lista:
			return True, a

	return False

cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}, {("q", False), ("r", False)}, {("p", True), ("q", False), ("r", False)}, {("p", False), ("q", False), ("r", False)}]

print(fuerzaBruta(cnf))