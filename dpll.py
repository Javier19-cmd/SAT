"""
Referencias: 
    1. https://davefernig.com/2018/05/07/solving-sat-in-python/
"""

def __select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]
 
def dpll(cnf, assignments={}):
 
    if len(cnf) == 0:
        return True, assignments
 
    if any([len(c)==0 for c in cnf]):
        return False, None
 
    l = __select_literal(cnf)
 
    new_cnf = [c for c in cnf if (l, True) not in c]
    new_cnf = [c.difference({(l, False)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat:
        return sat, vals
 
    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat:
        return sat, vals
 
    return False, None

#Pasando expresiones.
cnf = [{(1, True), (2, True), (3, True)},
         {(1, False), (2, True)},
            {(1, False), (3, True)},
                {(2, False), (3, True)},
                    {(1, True), (2, False)},
                        {(1, True), (3, False)},
                            {(2, True), (3, False)},
                                {(1, False), (2, False), (3, False)}]

print(dpll(cnf))