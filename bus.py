from itertools import combinations_with_replacement
import pprint 

import dsl

pp = pprint.PrettyPrinter(indent=2)

def args(dsl, op, w, E):
    E_acc = []
    for i, es in E.items():
        for e in es:
            t = (i, e[1])
            E_acc.append(t)

    v_all = list(combinations_with_replacement(E_acc, dsl.arity(op)))

    acc = []
    for v in v_all:
        t_w = 0
        t_acc = []
        for v_p in v:
            t_w += v_p[0]
            t_acc.append(v_p[1])
    
        if t_w == w:
            acc.append(t_acc)
            
    return acc

def find_term(E, V):
    for e in list(E.values()):
        for el in e:
            if V == el[0]:
                return True
    
    return False

def bus(dsl, io, depth=10, debug=0):

    inps = [io[i][0] for i in range(len(io))]
    oups = [io[i][1] for i in range(len(io))]

    E = {}
    C = dsl.extract_constants(io)
    E[1] = C
    E[1] += [[[input[0][i] for input in io], ["input", i]] for i in range(len(io[0][0]))]
    
    for w in range(2, depth):
        if (debug >= 1):
            print(f"Depth: {w}")
        E[w] = []
        for op in dsl.ops():
            n = dsl.arity(op)
            A = args(dsl, op, w-1, E)

            for a in A:
                try:
                    V = dsl.execute([op, a], inps)
                except Exception as error:
                    if (debug >= 2):
                        print(error)
                    continue

                if (debug >= 1): 
                    print([op, a])
            
                if not find_term(E, V):
                    E[w].append([V, [op, a]])

                if V == oups:
                    return [op, a]
    return "Not_found"

io = [
       [[2, 10], 20], 
       [[4, 4], 16], 
       [[7, 12], 84], 
     ]

print(bus(dsl.ArithDsl(), io, debug=0))