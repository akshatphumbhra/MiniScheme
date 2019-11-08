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

def isNumber(inputList):
    digits = [1,2,3,4,5,6,7,8,9,0]
    if len(inputList) == 1 and inputList[0] in digits:
        return True
    return False

def isSymbol(inputList):
    if len(inputList) == 1 and not isNumber(inputList):
        return True
    return False

def newLitExp(inputList):
    answer = ["lit-exp", inputList[0]]
    return answer

def newVarRef(inputList):
    answer = ["var-ref", inputList[0]]
    return answer

def isLitExp(inputList):
    if type(inputList) is list:
        return inputList[0] == "lit-exp"
    return False

def litExpNum(inputList):
    return inputList[1]

def newLetExp(inputList):
    result = list(map(car, inputList[1]))
    result2 = list(map(parse,list(map(cadr, inputList[1]))))
    result3 = parse(inputList[2])
    answer = ["let-exp", result, result2, result3]
    return answer

def car(inputList):
    return inputList[0]

def isLetExp(inputList):
    if type(inputList) is list:
        return inputlist[0] == "let-exp"
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
