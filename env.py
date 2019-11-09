import sys
from functions import car
#Datatype definitions and environment variables

def printError(message, var=""):
    if not var:
        print(message)
    else:
        print(message, var)
    sys.exit(1)

def isEmptyEnv(env):
    if type(env) is list:
        return env[0] == "empty-env"
    return False

def isExtendedEnv(env):
    if type(env) is list:
        return env[0] == "extended-env"
    return False

def isEnv(env):
        return isEmptyEnv(env) or isExtendedEnv(env)

def emptyEnv():
    return ["empty-env"]

def extendedEnv(symbols, values, oldEnv):
    return ["extended-env", symbols, values, oldEnv]

def symbols(env):
    if isExtendedEnv(env):
        return env[1]
    else:
        printError("symbols: Bad environment")

def values(env):
    if isExtendedEnv(env):
        return env[2]
    else:
        printError("values: Bad environment")

def oldEnv(env):
    if isExtendedEnv(env):
        return env[3]
    else:
        printError("old environment: Bad environment")

def lookup(env, symbol):
    if len(symbols(env)) == 0 and isEmptyEnv(oldEnv(env)):
        printError("apply env: no binding for", symbol)
    elif (len(symbols(env))) == 0:
        return lookup(oldEnv(env), symbol)
    elif symbols(env)[0] == symbol:
        return values(env)[0]
    else:
        return lookup(extendedEnv(symbols(env)[1:], values(env)[1:], oldEnv(env)), symbol)

#Data structures for different types of grammar in the Scheme Language

#------Literal Expressions (eg. numbers)----------
def newLitExp(inputList):
    answer = ["lit-exp", inputList[0]]
    return answer

def isLitExp(inputList):
    if type(inputList) is list:
        return inputList[0] == "lit-exp"
    return False

def litExpNum(inputList):
    return inputList[1]
#-----------------------------------------------

#-----Variable References (eg. All symbols) -------
def newVarRef(inputList):
    answer = ["var-ref", inputList[0]]
    return answer

def isVarRef(inputList):
    if type(inputList) is list:
        return inputList[0] == "var-ref"
    return False

def varRefSymbol(inputList):
    return inputList[1]
#----------------------------------------------

#Data types for primitive operators-------------
primitiveOperators= ['+', '-', '*' , '/' , 'add1' , 'sub1' ,'minus' , 'first' , 'rest' , 'build' , 'list' , 'empty?' , 'equals?', 'lt?', 'gt?', 'leq?', 'geq?']

def newPrimProc(inputList):
    return ["prim-proc", inputList]

def primProcSymbol(inputList):
    return inputList[1]

def isPrimProc(inputList):
    if type(inputList) is list:
        return inputList[0] == "prim-proc"
    return False

def newAppExp(proc, args):
    return ["app-exp", proc, args]

def isAppExp(inputList):
    if type(inputList) is list:
        return inputList[0] == "app-exp"
    return False

def appProc(inputList):
    return inputList[1]

def appArgs(inputList):
    return inputList[2]

#----------------------------------------


#--------Initial environment--------------------------

initEnv = extendedEnv(primitiveOperators, list(map(newPrimProc, primitiveOperators)), extendedEnv(["x", "y", "nil"], [10, 23, []], emptyEnv()))
#------------------------------------------------------
