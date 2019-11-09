
def isNumber(inputList):
    #print(inputList)
    if isinstance(inputList, int) or (len(inputList)==1 and isinstance(inputList[0], int)):
        return True
    return False

def isSymbol(inputList):
    if isinstance(inputList,str) or (len(inputList)==1 and isinstance(inputList[0], str)):
        return True
    return False

def car(inputList):
    return inputList[0]

def cadr(inputList):
    return inputList[1]
