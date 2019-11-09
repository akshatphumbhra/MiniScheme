from env import *
from parse import *
from interp import *
from makeList import *

def main():
    done = False
    while not done:
        command = input("MS> ")
        if command == "exit":
            done = True
            break
        commandList = convertToList(command)
        print(commandList)
        print(evalExp(parse(commandList), initEnv))

if __name__ == "__main__":
    main()
