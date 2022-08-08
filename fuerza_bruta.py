"""
1. Algoritmo de fuerza bruta: https://davefernig.com/2018/05/07/solving-sat-in-python/
"""
import itertools

def fuerza_bruta(cnf):
    literales = set() # Conjunto que guardará las literales.
    for conj in cnf: # Recorremos la lista de conjunciones. 
        for disj in conj: # Recorremos la lista de disyunciones.
            literales.add(disj[0]) # Añadimos la literal a la lista.
 
    #Se convierte el conjunto en una lista para poder iterar sobre ella.
    literales = list(literales)
    n = len(literales)

    for seq in itertools.product([True,False], repeat=n): # Generamos todas las posibles combinaciones de literales.
        a = set(zip(literales, seq)) # Se crea un conjunto con las literales y sus valores.
        if all([bool(disj.intersection(a)) for disj in cnf]): # Se comprueba si la combinación de literales es satisfactoria.
            return True, a # Si lo es, se devuelve True.
 
    return False # Si no se ha encontrado ninguna combinación satisfactoria, se devuelve False.

#cnf = [{('a', False), ('b', False)}, {('a', False), ('b', False)}]

#cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}]

#cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}, {("q", False), ("r", False)}]

#cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}, {("q", False), ("r", False)}, {("p", True), ("q", False), ("r", False)}]

cnf = [{("p", False), ("q", True)}, {("p", False), ("r", False)}, {("q", False), ("r", False)}, {("p", True), ("q", False), ("r", False)}, {("p", False), ("q", False), ("r", False)}]

print(fuerza_bruta(cnf))