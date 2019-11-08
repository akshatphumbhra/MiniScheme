from env import *
from functions import *

def parse(inputList):
    if isNumber(inputList):
        return newLitExp(input)
    elif isSymbol(inputList):
        return newVarRef(input)
    elif inputList[0] == "let":
        return newLetExp(inputList)
    elif inputList[0] == "if":
        return newIfExp(inputList)
    elif type(inputList) is list:
        pass
    else:
        return newAppExp(parse(inputList[0]), map(parse, inputList[1:]))
