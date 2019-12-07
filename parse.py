from env import *
from functions import *

def parse(inputList):
    if isNumber(inputList):
        if isinstance(inputList, int):
            return newLitExp([inputList])
        return newLitExp(inputList)
    elif isSymbol(inputList):
        if isinstance(inputList, str):
            if inputList.isdigit():
                return newLitExp([int(inputList)])
            return newVarRef([inputList])
        return newVarRef(inputList)
    elif inputList[0] == "let":
        return newLetExp(inputList)
    elif inputList[0] == "if":
        return newIfExp(inputList)
    elif inputList[0] == "lambda":
        return newLambdaExp(inputList)
    elif type(inputList) is not list:
        printError("parse: Invalid syntax", inputList)
    else:
        return newAppExp(parse(inputList[0]), list(map(parse, inputList[1:])))
    
#data types for closure-----------------------------
def newClosure(params, body, env):
    answer = ["closure", params, body, env]
    return answer

def closureParams(inputList):
    return (inputList[1])

def closureBody(inputList):
    return (inputList[2])

def closureEnv(inputList):
    return (inputList[3])

def isClosure(inputList):
    if type(inputList) is list:
        return inputList[0] == "closure"
    return False

#data types for Lambda ----------------------------
def newLambdaExp(inputList):
    answer = ["lambda-exp", inputList[1], parse(inputList[2])]
    return answer

def lambdaParams(inputList):
    return inputList[1]

def lambdaBody(inputList):
    return inputList[2]

def isLambdaExp(inputList):
    if type(inputList) is list:    
        return inputList[0] == "lambda-exp"
    return False

#Data types for if, let ---------------------------
def newLetExp(inputList):
    result = list(map(car, inputList[1]))
    result2 = list(map(parse,list(map(cadr, inputList[1]))))
    result3 = parse(inputList[2])
    answer = ["let-exp", result, result2, result3]
    return answer

def isLetExp(inputList):
    if type(inputList) is list:
        return inputList[0] == "let-exp"
    return False

def letSymbols(inputList):
    return inputList[1]

def letValues(inputList):
    return inputList[2]

def letBody(inputList):
    return inputList[3]

def newIfExp(inputList):
    answer = ["if-exp", list(map(parse, inputList[1:]))]
    return answer

def isIfExp(inputList):
    if type(inputList) is list:
        return inputList[0] == "if-exp"
    return False

def ifCondition(inputList):
    return inputList[1][0]

def ifTrueExp(inputList):
    return inputList[1][1]

def ifFalseExp(inputList):
    return inputList[1][2]
#-----------------------------------------------------
