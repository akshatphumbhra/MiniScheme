from parse import *
from env import *

def applyPrimitiveOp(op, argValues):
    if op == "+":
        return argValues[0] + argValues[1]
    elif op == "-":
        return argValues[0] - argValues[1]
    elif op == "*":
        return argValues[0] * argValues[1]
    elif op == "/":
        return argValues[0] / argValues[1]
    elif op == "add1":
        return argValues[0] + 1
    elif op == "sub1":
        return argValues[0] - 1
    elif op == "minus":
        return argValues[0] - 2*argValues[0]
    elif op == "list":
        return argValues
    elif op == "build":
        if type(argValues[1]) is list:
             argValues[1].insert(0, argValues[0])
             return argValues[1]
        else:
            return [argValues[0], argValues[1]]
    elif op == "first":
        return argValues[0][0]
    elif op == "rest":
        return argValues[0][1:]
    elif op == "equals?":
        return argValues[0] == argValues[1]
    elif op == "lt?":
        return argValues[0] < argValues[1]
    elif op == "gt?":
        return argValues[0] > argValues[1]
    elif op == "leq?":
        return argValues[0] <= argValues[1]
    elif op == "geq?":
        return argValues[0] >= argValues[1]
    elif op == "empty?":
        return len(argValues[0]) == 0

def applyProc(p, argValues):
    #print(p, argValues)
    if isPrimProc(p):
        return applyPrimitiveOp(primProcSymbol(p), argValues)
    else:
        printError("applyProc: Bad Procedure", p)

def evalExp(tree, env):
    if isLitExp(tree):
        return litExpNum(tree)
    elif isVarRef(tree):
        return lookup(env, varRefSymbol(tree))
    elif isLetExp(tree):
        return evalExp(letBody(tree), extendedEnv(letSymbols(tree), list(map(lambda x: evalExp(x, env), letValues(tree))), env))
    elif isIfExp(tree):
        if evalExp(ifCondition(tree),env):
            return evalExp(ifTrueExp(tree), env)
        else:
            return evalExp(ifFalseExp(tree), env)
    elif isAppExp(tree):
        return applyProc(evalExp(appProc(tree), env), list(map(lambda t: evalExp(t,env), appArgs(tree))))
    else:
        printError("evalExp: Invalid tree", tree)
