
def parseIntoList(inputVal):
    answer = []
    i=0
    while i <= (len(inputVal)):
        if inputVal[i] == ")":
            return answer, i+1

        elif inputVal[i] == "(":
            retVal, index = parseIntoList(inputVal[i+1:])
            i = i +index
            #print(i)
            answer.append(retVal)
        else:
            answer.append(inputVal[i])
        i+=1
# ( if ( < 4 6 ) ( + 3 4 ) ( * 4 5 ) )
# split == ['(', 'if', '(', '<', '4' , '6', ')','(', '*', '4' , '5' , ')', ')']

def convertToList(command):
    if '(' not in command:
        if command.isdigit():
            return [int(command)]
        else:
            return [command]
    value=""
    for letter in command:
        if letter == "(":
            value = value + letter + " "
        elif letter == ")":
            value = value + " " +")"
        else:
            value+= letter
    commandList = value.split()
    answer, i = parseIntoList(commandList[1:])
    return answer
