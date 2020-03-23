
from AVL.Node import Node
class BalancedTree(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):

        parentNode = self.rootNode

        if self.rootNode  ==  None:
            parentNode = Node(data, None)
            self.rootNode = parentNode
        else:
            parentNode = self.rootNode.insert(data,self.rootNode)

        self.rebalanceTree(parentNode)

    def rebalanceTree(self, parentNode):
        self.setBalance(parentNode)

    def setBalance(self, node):
        node.balance = (self.height(node.leftChild) - self.height(node.rightChild))

    def height(self, node):
        if node == None:
            return -1
        else:
            return 1 + max(self.height(node.leftChild), self.height(node.rightChild))

    def traverseInOrder(self):
            if self.rootNode:
                self.rootNode.traverseInOrder()