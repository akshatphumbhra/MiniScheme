
#input scheme (if-exp (eq? 3 (+ 2 1)) (5) (20))
#desired output [if-exp, [eq?, 3, [+ , 2, 1] ], [5], [20]]

python = []

def main():
    scheme = input("Enter a scheme expression: ")
    schemeExp = scheme.split("(") #make input into ['', 'if-exp ', 'eq? 3 ', '+ 2 1)) ', '5) ', '20))']
    i = 0
    for word in schemeExp:    #turn list into [[], ['if-exp'], ['eq?', '3'], ['+', '2', '1))'], ['5)'], ['20))']]
        schemeExp[i] = word.split()
        i += 1
    print(schemeExp)
    #final = toPython(scheme)
    #print(final)

    

# for letter in scheme:
#     if (letter == "(" ):
#         python += ["["+letter+"]"]
#     else:
#         python += letter
        
def toPython(scheme):
    if (scheme[0][0] == "("):
            return python.extend([toPython(scheme[1:len(scheme)])])
    else:
        for i in scheme[0]:
            if (i == ")"):
                return
            else:
                python.append(i)
                return toPython(scheme[1:len(scheme)])
        
    
    
main()