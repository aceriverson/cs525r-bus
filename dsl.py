class Dsl(object):
    def __init__(self):
        pass

    def arity(self, op):
        pass

    def execute(self, expr, inps):
        pass

    def extract_constants(self, io):
        pass

    def ops(self):
        pass


class ArithDsl(Dsl):
    def __init__(self):
        super().__init__()
        

    def arity(self, op):
        ops_arity = {
            "plus": 2,
            "minus": 2,
            "mult": 2,
            "div": 2,
            "neg": 1
        }

        return ops_arity[op]
    
    def execute(self, expr, inps):
        if expr[0] == "plus":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)

            acc = []
            for i in range(len(a0)):
                acc.append(a0[i] + a1[i])
            
            return acc
        
        elif expr[0] == "minus":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)

            acc = []
            for i in range(len(a0)):
                acc.append(a0[i] - a1[i])
            
            return acc
        
        elif expr[0] == "mult":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)

            acc = []
            for i in range(len(a0)):
                acc.append(a0[i] * a1[i])
            
            return acc
        
        elif expr[0] == "div":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)

            acc = []
            for i in range(len(a0)):
                acc.append(a0[i] / a1[i])
            
            return acc
        
        elif expr[0] == "neg":
            a0 = self.execute(expr[1][0], inps)

            acc = []
            for i in range(len(a0)):
                acc.append(a0[i] * -1)
            
            return acc
    
        elif expr[0] == "input":
            acc = []
            for i in range(len(inps)):
                acc.append(inps[i][expr[1]])

            return acc
        
        elif expr[0] == "constant":
            return [expr[1] for i in range(len(inps))]
        
        
        else:
            raise ValueError(expr)

    def extract_constants(self, io):
        oups = [io[i][1] for i in range(len(io))]
        return [[[c for _ in range(len(io))], ["constant", c]] for c in oups]
    
    def ops(self):
        return [
            "plus",
            "minus",
            "mult",
            "div",
            "neg"
        ]
    

class StringDsl(Dsl):
    def __init__(self):
        super().__init__()

    
    def arity(self, op):
        ops_arity = {
            "Concat": 2,
            "Left": 2,
            "Right": 2,
            "Substr": 3,
            "Replace": 4,
            "Trim": 1,
            "Repeat": 2,
            "Substitute1": 3,
            "Substitute2": 4,
            "ToText": 1,
            "Lowercase": 1,
            "Uppercase": 1,
            "Propercase": 1,
            "Plus": 2,
            "Minus": 2,
            "Find1": 2,
            "Find2": 3,
            "Len": 1
        }

        return ops_arity[op]
    

    def execute(self, expr, inps):
        if expr[0] == "Concat":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            return [a0[i] + a1[i] for i in range(len(inps))]
        elif expr[0] == "Left":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            return [a0[i][:a1[i]] for i in range(len(inps))]
        elif expr[0] == "Right":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            return [a0[i][-a1[i]:] for i in range(len(inps))]
        elif expr[0] == "Substr":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            a2 = self.execute(expr[1][2], inps)
            return [a0[i][a1[i]:a2[i]] for i in range(len(inps))]
        elif expr[0] == "Replace":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            a2 = self.execute(expr[1][2], inps)
            a3 = self.execute(expr[1][3], inps)
            return [a0[i][:a1[i]] + a3[i] + a0[i][a2[i]:] for i in range(len(inps))]
        elif expr[0] == "Trim":
            a0 = self.execute(expr[1][0], inps)
            return [a0[i].strip() for i in range(len(inps))]
        elif expr[0] == "Repeat":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            return [a0[i] * a1[i] for i in range(len(inps))]
        elif expr[0] == "Substitute1":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            a2 = self.execute(expr[1][2], inps)
            return [a0[i].replace(a1[i], a2[i]) for i in range(len(inps))]
        elif expr[0] == "Substitute2":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            a2 = self.execute(expr[1][2], inps)
            a3 = self.execute(expr[1][3], inps)
            return [a0[i].replace(a1[i], a2[i], a3[i]) for i in range(len(inps))]
        elif expr[0] == "ToText":
            a0 = self.execute(expr[1][0], inps)
            return [int(a0[i]) for i in range(len(inps))]
        elif expr[0] == "Lowercase":
            a0 = self.execute(expr[1][0], inps)
            return [a0[i].lower() for i in range(len(inps))]
        elif expr[0] == "Uppercase":
            a0 = self.execute(expr[1][0], inps)
            return [a0[i].upper() for i in range(len(inps))]
        elif expr[0] == "Propercase":
            a0 = self.execute(expr[1][0], inps)
            return [a0[i].title() for i in range(len(inps))]
        elif expr[0] == "Plus":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            return [a0[i] + a1[i] for i in range(len(inps))]
        elif expr[0] == "Minus":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            return [a0[i] - a1[i] for i in range(len(inps))]
        elif expr[0] == "Find1":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            return [a0[i].find(a1[i]) for i in range(len(inps))]
        elif expr[0] == "Find2":
            a0 = self.execute(expr[1][0], inps)
            a1 = self.execute(expr[1][1], inps)
            a2 = self.execute(expr[1][2], inps)
            return [a0[i].find(a1[i], a2[i]) for i in range(len(inps))]
        elif expr[0] == "Len":
            a0 = self.execute(expr[1][0], inps)
            return [len(a0[i]) for i in range(len(inps))]
        elif expr[0] == "constant":
            return [expr[1] for i in range(len(inps))]
        elif expr[0] == "input":
            return [inps[i][expr[1]] for i in range(len(inps))]
        else:
            raise ValueError(expr)


    def extract_constants(self, io):
        oups = [io[i][1] for i in range(len(io))]

        max_i = 0
        for w in oups:
            if len(w) > max_i:
                max_i = len(w)

        

        return [[[c for _ in range(len(io))], ["constant", c]] for c in oups] + [[[i for _ in range(len(io))], ["constant", i]] for i in range(max_i)]

    def ops(self):
        return [
            "Concat",
            "Left",
            "Right",
            "Substr",
            "Replace",
            "Trim",
            "Repeat",
            "Substitute1",
            "Substitute2",
            "ToText",
            "Lowercase",
            "Uppercase",
            "Propercase",
            "Plus",
            "Minus",
            "Find1",
            "Find2",
            "Len"
        ]
    

class SchemeDsl(Dsl):
    def __init__(self):
        super().__init__()

    def arity(self, op):
        ops_arity = {
            "'cons": 2,
            "'car": 1,
            "'cdr": 1,
            "'not": 1,
            "'add1": 1,
            "'+": 2,
            "'*": 2,
            "'append": 2,
            "'apply1": 2,
            "'apply": 2
        }

        return ops_arity[op]

    def execute(self, expr, inps):
        pass

    def extract_constants(self, io):
        pass

    def ops(self):
        return [
            "'cons",
            "'car",
            "'cdr",
            "'not",
            "'add1",
            "'+",
            "'*",
            "'append",
            "'apply1",
            "'apply"
        ]