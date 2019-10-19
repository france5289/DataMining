from Node import Node
class FPTree():
    def __init__(self, node=None):
        '''
        constructor for Tree object
        it can receive a Node object which will be the root node of the tree \n
        Parameter:
            node(optional)(Node obj.)
            if node parameter value is None, then it will create a NULL node as root node \n
        Return: none
        '''
        self.__root = Node() if type(node) is None else node
    #-----------Getter-----------
    def GetRoot(self):
        '''
        Return root node of FPTree \n
        Parameter : none \n
        Return : Node object \n
        '''
        return self.__root
    #-----------Getter-----------
    
    #-----------Setter-----------
    def ContructPatternPath(self, startnode, pattern):
        '''
        contruct pattern path from root node \n
        if startnode is None then it start from root node \n
        Parameter: \n
            pattern(lits of sets)
            startnode(Node obj.)
        '''
        if startnode is None:
            startnode = self.__root
        
            
                
    #-----------Setter-----------
    

if __name__ == '__main__':
    # FPTree.InsertPattern(parentnode=a.getroot(), {1,2,3})
    pass