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
        self.__root = Node(level=1) if node is None else node
        self.__headerTable = dict() # this table record position of a Node obj.
        # e.g                    root 
        #                       /
        #               <Node.obj( item = 'Bread' ) at 0x10ab53b90> 
        # self.__headerTable :  { 'Bread': [ <Node.obj at 0x10ab53b90 ] }
    def __str__(self):
        return self.__root.__str__()
    #-----------Getter-----------
    def GetRoot(self):
        '''
        Return root node of FPTree \n
        Parameter : none \n
        Return : Node object \n
        '''
        return self.__root
    def GetHeaderTable(self):
        '''
        Return header Table of FPTree \n
        Parameter : none \n
        Return : dict with {key:value} = { Node.item(str) : list of Node object(list) }
        '''
        return self.__headerTable
    #-----------Getter-----------
    #-----------Setter-----------


    def ContructPatternPath(self, startnode, pattern):
        '''
        contruct pattern path from root node \n
        if startnode is None then it start from root node \n
        this function is recursive function with base case when pattern is empty \n
        Parameter: \n
            pattern(lits of string)
            startnode(Node obj.)
        '''
        # base case
        if len(pattern) == 0:
            return
        if startnode is None: # start from root
            startnode = self.__root
        insert_item = pattern.pop(0) # it is a string
        # check insert_itemset is startnode's child or not
        for child in startnode.getChilds():
            if child.getItem() == insert_item:
                child.addSupCount(1)
                return self.ContructPatternPath(startnode = child, pattern=pattern)
        # if insert_itemset is not startnode's child
        newnode = Node(item=insert_item, supcnt=1, parent=startnode, level=startnode.getNodeLevel() + 1)
        startnode.addChild(newnode)
        return self.ContructPatternPath(startnode=newnode, pattern=pattern)

    #-----------Setter-----------
    

if __name__ == '__main__':
    Tree = FPTree()
    transactions = [    ['Bread', 'Milk', 'Beer'], 
                        ['Bread', 'Coffee'],
                        ['Bread', 'Egg'],
                        ['Bread', 'Milk', 'Coffee'],
                        ['Milk', 'Egg'],
                        ['Bread', 'Milk', 'Egg', 'Beer'],
                        ['Bread', 'Milk', 'Egg'] ] 
    for tranc in transactions:
        Tree.ContructPatternPath(startnode = None,pattern = tranc)

    print(Tree.__str__())