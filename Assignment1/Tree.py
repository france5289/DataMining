from Node import Node
class Tree():
    def __init__(self, node=None):
        '''
        constructor for Tree object
        it can receive a Node object which will be the root node of the tree
        Parameter:
            node(optional)(Node obj.)
            if node parameter value is None, then it will create a NULL node as root node
        Return: none
        '''
        if type(node) is not None and type(node) is not Node:
            raise ValueError('Tree constructor just receive Node object as parameter!')
        self.__root = Node() if type(node) is None else node

    
