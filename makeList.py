from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    def postorder(tree):
        if tree != None:
            postorder(tree.getLeftChild())
            postorder(tree.getRightChild())
            print(tree.getRootVal())

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.preorder()  #defined and explained in the next section
pStack = Stack()
def func(takein):
    openParen = False
    value = ""
    result = list()
    for i in range(len(takein)):
        if takein[i] == '(' and not openParen:
            openParen = True
            
def parseIntoList():
    takein = ""
    while takein != "exit":
        takein = input("MS> ")
        answer= buildParseTree(takein)
        answer.postorder()
parseIntoList()
