
def isNumber(inputList):
    digits = [1,2,3,4,5,6,7,8,9,0]
    if len(inputList) == 1 and inputList[0] in digits:
        return True
    return False

def isSymbol(inputList):
    if len(inputList) == 1 and not isNumber(inputList):
        return True
    return False

def car(inputList):
    return inputList[0]
