"""
Referencias: 
    1. https://davefernig.com/2018/05/07/solving-sat-in-python/
"""

def __select_literal(cnf): #Obtiene el literal con menor cantidad de apariciones en la clausula.
    for c in cnf:
        for literal in c:
            return literal[0]
 
def dpll(cnf, assignments={}): #Algoritmo DPLL
 
    if len(cnf) == 0: #Si la clausula es vacia, se retorna True.
        return True, assignments
 
    if any([len(c)== 0 for c in cnf]): #Si alguna clausula es vacia, se retorna False.
        return False, None
 
    l = __select_literal(cnf) #Se obtiene el literal con menor cantidad de apariciones en la clausula.
    
    #Se obtiene el valor de verdad del literal.
    new_cnf = [c for c in cnf if (l, True) not in c]

    # print(new_cnf)

    new_cnf = [c.difference({(l, False)}) for c in new_cnf]

    # print(new_cnf)

    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat: #Si el valor de verdad es True, se retorna True.
        return sat, vals
    
    #Se obtiene el valor de verdad del literal.
    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat: #Si el valor de verdad es False, se retorna False.
        return sat, vals
 
    return False, None

cnf = [{("f", False), ("p", False), ("q", False)}] #Se define la clausula.

print(dpll(cnf)) #Se imprime el resultado.