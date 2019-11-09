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
    elif type(inputList) is not list:
        printError("parse: Invalid syntax", inputList)
    else:
        return newAppExp(parse(inputList[0]), list(map(parse, inputList[1:])))

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
    return inputList[1]

def ifTrueExp(inputList):
    return inputList[2]

def ifFalseExp(inputList):
    return inputList[3]
#-----------------------------------------------------
